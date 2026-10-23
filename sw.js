// Kopia mapy w telefonie: najpierw sieć (świeże dane), a gdy jej brak albo jest zbyt wolna – ostatnia zapisana wersja.
// Podkłady (OSM, ortofoto, cieniowanie) i zgłaszanie uwag nadal wymagają połączenia.
// Nowy plik strony albo danych trzeba dopisać do listy PLIKI.
const KOPIA = 'wilga-mapa-2', CZEKAJ_MS = 4000;
const PLIKI = ['./', 'wilga.css', 'map-ui.css', 'znak.svg', 'manifest.webmanifest', 'wilga-osmand.gpx',
  'lib/leaflet/leaflet.min.js', 'lib/leaflet-rotate/leaflet-rotate.js', 'lib/leaflet/leaflet.min.css', 'lib/leaflet/images/layers.png', 'lib/leaflet/images/layers-2x.png',
  ...['adresy', 'budynki', 'drogi', 'hydranty', 'miejsca', 'siatka', 'stromizny', 'woda_cieki', 'woda_obszary', 'zawracanie', 'obreby'].map(n => `data/${n}.geojson`),
  'data/indeks.json', 'data/dzialki.json', 'data/stan.json',
  ...['hydrant', 'hydrant_do_weryfikacji', 'zbiornik', 'swietlica', 'strzalka_spadek_1', 'strzalka_spadek_2', 'strzalka_spadek_3'].map(n => `ikony/${n}.svg`),
  'ikony/app-192.png'];

self.addEventListener('install', e => e.waitUntil(caches.open(KOPIA).then(c => c.addAll(PLIKI)).then(() => self.skipWaiting())));
self.addEventListener('activate', e => e.waitUntil(self.clients.claim()));

self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET' || new URL(e.request.url).origin !== location.origin) return;
  e.respondWith((async () => {
    const c = await caches.open(KOPIA), zapisana = await c.match(e.request, { ignoreSearch: true });
    const siec = fetch(e.request).then(r => { if (r.ok) c.put(e.request, r.clone()); return r; });
    if (!zapisana) return siec;
    e.waitUntil(siec.catch(() => {})); // przy słabym zasięgu odpowiedź z sieci dojdzie później i odświeży kopię
    const r = await Promise.race([siec.catch(() => null), new Promise(k => setTimeout(k, CZEKAJ_MS))]);
    return r && r.ok ? r : zapisana;
  })());
});
