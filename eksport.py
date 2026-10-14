# Eksport warstw projektu do GeoJSON dla strony (uruchamiać w konsoli Pythona QGIS):
#   exec(open('C:/Users/golia/wilga-mapa/web/eksport.py', encoding='utf8').read())
import json, re, os, datetime
from qgis.core import (QgsProject, QgsVectorLayer, QgsCoordinateReferenceSystem,
                       QgsCoordinateTransform, QgsFeatureRequest, QgsGeometry)

OUT = 'C:/Users/golia/wilga-mapa/web/data'
os.makedirs(OUT, exist_ok=True)
prj = QgsProject.instance()
WGS = QgsCoordinateReferenceSystem('EPSG:4326')


def tag(tags, k):
    m = re.search(r'"%s"=>"([^"]*)"' % k, tags or '')
    return m.group(1) if m else None


def dump(layer, name, props, expr=None, prec=6):
    tr = QgsCoordinateTransform(layer.crs(), WGS, prj)
    req = QgsFeatureRequest()
    if expr:
        req.setFilterExpression(expr)
    feats = []
    for f in layer.getFeatures(req):
        g = QgsGeometry(f.geometry())
        if g.isEmpty():
            continue
        g.transform(tr)
        feats.append({'type': 'Feature', 'properties': props(f),
                      'geometry': json.loads(g.asJson(prec))})
    with open(f'{OUT}/{name}.geojson', 'w', encoding='utf8') as fo:
        json.dump({'type': 'FeatureCollection', 'features': feats}, fo, ensure_ascii=False, separators=(',', ':'))
    print(name, len(feats))


L = lambda n: prj.mapLayersByName(n)[0]

dump(L('drogi'), 'drogi', lambda f: {
    'n': f['nazwa'], 'k': f['kategoria'], 'u': tag(f['other_tags'], 'weryfikacja')})
dump(L('hydranty_reczne'), 'hydranty', lambda f: {'t': f['typ'], 'u': f['uwagi']})
dump(L('stromizny'), 'stromizny', lambda f: {
    'n': f['ulica'], 's': f['spadek_proc'], 'k': f['klasa'], 'a': f['azymut_pod_gore'],
    'l': f['dlugosc_m'], 'c': f['komorka']})
dump(L('miejsca_charakterystyczne'), 'miejsca', lambda f: {'n': f['nazwa'], 't': f['typ']})
dump(L('miejsca_zawracania'), 'zawracanie', lambda f: {})
dump(L('woda_obszary'), 'woda_obszary', lambda f: {'n': f['nazwa']}, prec=5)
dump(L('woda_cieki'), 'woda_cieki', lambda f: {'n': f['nazwa'], 't': f['typ']}, prec=5)
dump(L('siatka_odniesienia'), 'siatka', lambda f: {'c': f['kod']})
dump(L('budynki'), 'budynki', lambda f: {}, prec=6)

prg = QgsVectorLayer('C:/Users/golia/wilga-mapa/data/prg/PRG_PunktyAdresowe_140313.shp', 'prg', 'ogr')
prg.setCrs(QgsCoordinateReferenceSystem('EPSG:2180'))
dump(prg, 'adresy', lambda f: {'u': f['NAZWA_ULC'], 'n': f['NUMER_PORZ']},
     expr="\"ID_SIMC\"='0694095' AND \"NAZWA_ULC\" != 'Wilgi'")

# adresy, których nie ma w PRG, a potwierdził je mieszkaniec (położenie z OSM): ulica, numer, lon, lat
POZA_PRG = [('Lipowa', '12', 21.431453, 51.843599)]
with open(f'{OUT}/adresy.geojson', encoding='utf8') as fi:
    adresy = json.load(fi)
adresy['features'] += [{'type': 'Feature', 'properties': {'u': u, 'n': n},
                        'geometry': {'coordinates': [x, y], 'type': 'Point'}} for u, n, x, y in POZA_PRG]
# domy na terenie osiedla, które w PRG należą do miejscowości Skurcza (adres bez ulicy, np. „Skurcza 60”, uwaga nr 16)
siat = L('siatka_odniesienia')
tr_s, tr_w = QgsCoordinateTransform(siat.crs(), prg.crs(), prj), QgsCoordinateTransform(prg.crs(), WGS, prj)
komorki = []
for f in siat.getFeatures():
    g = QgsGeometry(f.geometry()); g.transform(tr_s); komorki.append((f['kod'], g))
skurcza = {}
for f in prg.getFeatures(QgsFeatureRequest().setFilterExpression("\"ID_SIMC\"='0694072'")):
    kom = next((k for k, g in komorki if g.contains(f.geometry())), None)
    if kom:
        p = tr_w.transform(f.geometry().asPoint())
        adresy['features'].append({'type': 'Feature', 'properties': {'u': 'Skurcza', 'n': f['NUMER_PORZ']},
                                   'geometry': {'coordinates': [round(p.x(), 6), round(p.y(), 6)], 'type': 'Point'}})
        skurcza.setdefault(kom, []).append(f['NUMER_PORZ'])
with open(f'{OUT}/adresy.geojson', 'w', encoding='utf8') as fo:
    json.dump(adresy, fo, ensure_ascii=False, separators=(',', ':'))

# indeks ulic: to samo źródło co indeks w atlasie A3
with open('C:/Users/golia/wilga-mapa/data/indeks_ulic_bloki.json', encoding='utf8') as fi:
    bloki = json.load(fi)
indeks = []
for b in bloki:
    nazwa, wiersze_txt = b[0], b[1:]
    if not wiersze_txt and ' — ' in nazwa:  # krótki wpis w jednej linii: "Biedronki — C7, nr 3"
        nazwa, reszta = nazwa.split(' — ', 1)
        wiersze_txt = [reszta.replace(', nr ', ' nr ')]
    wiersze = []
    for w in wiersze_txt:
        kom, _, nr = w.strip().partition(' nr ')
        wiersze.append({'k': [k.strip() for k in kom.split(',') if k.strip()], 'nr': nr or None})
    indeks.append({'u': nazwa, 'w': wiersze})
nr_klucz = lambda n: (int(re.match(r'\d+', n).group()), n)
gdzie = next(i for i, w in enumerate(indeks) if w['u'] > 'Skurcza' and w['u'][0] == 'S')  # indeks jest w polskiej kolejności
indeks.insert(gdzie, {'u': 'Skurcza (adres bez ulicy)', 'w': [{'k': [k], 'nr': ', '.join(sorted(n, key=nr_klucz))} for k, n in sorted(skurcza.items())]})
with open(f'{OUT}/indeks.json', 'w', encoding='utf8') as fo:
    json.dump(indeks, fo, ensure_ascii=False, separators=(',', ':'))
print('indeks', len(indeks))

# działki w siatce osiedla (indeks i wyszukiwarka): [numer, obręb, komórka, lon, lat] punktu wewnątrz działki
OBREBY = {'0010': 'Osiedle Wilga', '0019': 'Wilga', '0012': 'Skurcza', '0008': 'Nowy Żabieniec', '0014': 'Stary Żabieniec',
          '0002': 'Cyganówka', '0016': 'Trzcianka', '0011': 'Ruda Tarnowska'}
dz = L('dzialki')
tr_d = QgsCoordinateTransform(dz.crs(), WGS, prj)
kom_d = [(f['kod'], f.geometry()) for f in siat.getFeatures()]  # siatka i działki są w EPSG:2180
dzialki = []
for f in dz.getFeatures():
    p = f.geometry().pointOnSurface()
    kom = next((k for k, g in kom_d if g.contains(p)), None)
    if kom and f['NUMER_OBREBU'] in OBREBY:
        q = tr_d.transform(p.asPoint())
        dzialki.append([f['NUMER_DZIALKI'], f['NUMER_OBREBU'], kom, round(q.x(), 6), round(q.y(), 6)])
with open(f'{OUT}/dzialki.json', 'w', encoding='utf8') as fo:
    json.dump({'obreby': OBREBY, 'd': dzialki}, fo, ensure_ascii=False, separators=(',', ':'))
print('dzialki', len(dzialki))

with open(f'{OUT}/stan.json', 'w', encoding='utf8') as fo:
    json.dump({'stan_na': datetime.date.today().isoformat()}, fo)
