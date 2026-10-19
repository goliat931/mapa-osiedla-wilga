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
POZA_PRG = [('Lipowa', '12', 21.431453, 51.843599), ('Saperów', '1A', 21.401946, 51.821582),  # 1A: uwaga nr 35
            ('Cyganówka', '70', 21.44509, 51.85953),
            ('Śnieżki', '3', 21.444811, 51.831351),  # uwaga nr 73: tabliczka na bramie (zdjęcie), budynek obok punktu PRG „Śnieżki 4”
            ('Czeremchy', '1M', 21.405706, 51.828551)]  # uwaga nr 80
# punkty PRG przesunięte na właściwy budynek: (ulica, numer) -> lon, lat
PRZESUNIETE = {('Śnieżki', '20'): (21.444524, 51.833282)}  # uwaga nr 69: punkt PRG ok. 25 m od budynku  # uwaga nr 63: za rzeką od wsi, ok. 200 m na północ od G1, dojazd tylko od Garwolinki; punkt z PRG (budynek nr 70 w EGiB)
with open(f'{OUT}/adresy.geojson', encoding='utf8') as fi:
    adresy = json.load(fi)
for a in adresy['features']:
    k = (a['properties']['u'], a['properties']['n'])
    if k in PRZESUNIETE:
        a['geometry']['coordinates'] = list(PRZESUNIETE[k])
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
# Nowy Żabieniec w kolumnach G i H siatki (las osiągalny od osiedla, wyjątek jak Skurcza; prośba Dawida 16.10.2026)
zabieniec = {}
for f in prg.getFeatures(QgsFeatureRequest().setFilterExpression("\"ID_SIMC\"='0693977'")):
    kom = next((k for k, g in komorki if k[0] in 'GH' and g.contains(f.geometry())), None)
    if kom:
        u = f"{f['NAZWA_ULC']} (Nowy Żabieniec)" if f['NAZWA_ULC'] else 'Nowy Żabieniec'
        p = tr_w.transform(f.geometry().asPoint())
        wl = {'u': f['NAZWA_ULC'], 'm': 'Nowy Żabieniec'} if f['NAZWA_ULC'] else {'u': 'Nowy Żabieniec'}
        adresy['features'].append({'type': 'Feature', 'properties': {**wl, 'n': f['NUMER_PORZ']},
                                   'geometry': {'coordinates': [round(p.x(), 6), round(p.y(), 6)], 'type': 'Point'}})
        zabieniec.setdefault(u, {}).setdefault(kom, []).append(f['NUMER_PORZ'])
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
gdzie = next(i for i, w in enumerate(indeks) if w['u'] > 'Cyganówka')
indeks.insert(gdzie, {'u': 'Cyganówka (adres bez ulicy)', 'w': [{'k': ['G1'], 'nr': '70 (ok. 200 m na północ od G1, dojazd od Garwolinki)'}]})
for u, kom in sorted(zabieniec.items()):
    gdzie = next((i for i, w in enumerate(indeks) if w['u'] > u), len(indeks))  # „Ż” i tak trafia na koniec
    indeks.insert(gdzie, {'u': u, 'w': [{'k': [k], 'nr': ', '.join(sorted(n, key=nr_klucz))} for k, n in sorted(kom.items())]})
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

# obręby sąsiednie (granice i nazwy jak na geoportalu) ze scalenia działek; tylko wewnątrz siatki,
# bo poza nią działek nie mamy i granica byłaby urwana
rama = QgsGeometry.fromRect(siat.extent())
wew = QgsGeometry.fromRect(siat.extent().buffered(-5))  # bez krawędzi siatki, żeby nie dublować ramki
grupy = {}
for f in dz.getFeatures():
    if f['NUMER_OBREBU'] != '0010':
        grupy.setdefault(f['NAZWA_OBREBU'], []).append(f.geometry())
obreby = []
for n, gs in sorted(grupy.items()):
    g = QgsGeometry.unaryUnion(gs).buffer(1, 2).buffer(-1, 2).intersection(rama)  # bufor zamyka szczeliny między działkami
    if g.area() < 5e4:
        continue
    p = tr_d.transform(max(g.asGeometryCollection(), key=lambda c: c.area()).pointOnSurface().asPoint())
    gr = QgsGeometry(g.constGet().boundary()).intersection(wew).simplify(2)
    gr.transform(tr_d)
    obreby.append({'type': 'Feature', 'properties': {'n': n, 'p': [round(p.x(), 5), round(p.y(), 5)]},
                   'geometry': json.loads(gr.asJson(6))})
with open(f'{OUT}/obreby.geojson', 'w', encoding='utf8') as fo:
    json.dump({'type': 'FeatureCollection', 'features': obreby}, fo, ensure_ascii=False, separators=(',', ':'))
print('obreby', [o['properties']['n'] for o in obreby])

# GPX dla OsmAnd (także w Android Auto): drogi jako ślady w kolorach przejezdności, punkty jako waypointy
from xml.sax.saxutils import escape as esc
KOLOR_GPX = {'zielony': '#1e9e4a', 'żółty': '#f5c400', 'czerwony': '#e3141b'}
OPIS_K = {'zielony': 'przejezdna dla ciężkiego wozu', 'żółty': 'lekki wóz / do sprawdzenia', 'czerwony': 'nieprzejezdna'}
gpx = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<gpx version="1.1" creator="mapa-osiedle-wilga.goliat.dev" xmlns="http://www.topografix.com/GPX/1/1" xmlns:osmand="https://osmand.net">',
       f'<metadata><name>Mapa Osiedla Wilga dla służb ({datetime.date.today().isoformat()})</name></metadata>']
def wpt(lyr, nazwa, kolor):
    tr = QgsCoordinateTransform(lyr.crs(), WGS, prj)
    for f in lyr.getFeatures():
        if f.geometry().isEmpty():
            continue
        p = tr.transform(f.geometry().centroid().asPoint())
        gpx.append(f'<wpt lat="{p.y():.6f}" lon="{p.x():.6f}"><name>{esc(nazwa(f))}</name>'
                   f'<extensions><osmand:color>{kolor}</osmand:color></extensions></wpt>')
wpt(L('hydranty_reczne'), lambda f: {'hydrant': 'Hydrant', 'zbiornik_wodny': 'Zbiornik wodny'}.get(f['typ'], 'Hydrant do weryfikacji'), '#0050d0')
wpt(L('miejsca_zawracania'), lambda f: 'Miejsce do zawracania', '#7a3db8')
wpt(L('miejsca_charakterystyczne'), lambda f: f['nazwa'] or '', '#555555')
for u, n, x, y in POZA_PRG:
    gpx.append(f'<wpt lat="{y}" lon="{x}"><name>{esc(u)} {n}</name><extensions><osmand:color>#000000</osmand:color></extensions></wpt>')
dr = L('drogi')
tr = QgsCoordinateTransform(dr.crs(), WGS, prj)
for f in dr.getFeatures():
    g = QgsGeometry(f.geometry())
    if g.isEmpty():
        continue
    g.transform(tr)
    linie = g.asMultiPolyline() if g.isMultipart() else [g.asPolyline()]
    k = f['kategoria']
    gpx.append(f'<trk><name>{esc(f["nazwa"] or "droga bez nazwy")}</name><desc>{OPIS_K.get(k, "")}</desc>'
               f'<extensions><osmand:color>{KOLOR_GPX.get(k, "#9aa0a6")}</osmand:color><osmand:width>bold</osmand:width></extensions>')
    for lin in linie:
        gpx.append('<trkseg>' + ''.join(f'<trkpt lat="{p.y():.6f}" lon="{p.x():.6f}"/>' for p in lin) + '</trkseg>')
    gpx.append('</trk>')
gpx.append('</gpx>')
with open('C:/Users/golia/wilga-mapa/web/wilga-osmand.gpx', 'w', encoding='utf8') as fo:
    fo.write('\n'.join(gpx))
print('gpx', len(gpx))

with open(f'{OUT}/stan.json', 'w', encoding='utf8') as fo:
    json.dump({'stan_na': datetime.date.today().isoformat()}, fo)
