# Historia zmian mapy

Każda poprawka danych na mapie ma tu wiersz: skąd się wzięła (numer uwagi z arkusza „Uwagi do mapy Osiedla Wilga” albo inne źródło) i co zmieniono. Ten sam numer jest w opisie commita (`Uwaga nr 12: …`), więc `git log -- data/` pokazuje dokładne różnice w danych.

| Data | Źródło | Co zmieniono |
| --- | --- | --- |
| 2026-10-12 | Dawid Karczewski (mieszkaniec) | Dodany adres Lipowa 12 (dawna Pierogarnia Aniołowa i sklep): nie ma go w rejestrze PRG, położenie z OpenStreetMap. |
| 2026-10-14 | Uwaga nr 3 | Hydrant przy Trakcie Słonecznym (C7), przy znaku drogowym: w GESUT wpisany jako dwa włazy, naniesiony w miejscu drugiego włazu od przewodu. |
| 2026-10-14 | Uwaga nr 4 | Hydrant przy Trakcie Słonecznym (C6), naprzeciwko „Żubra”: w GESUT wpisany jako dwa włazy, naniesiony w miejscu drugiego włazu od przewodu. |
| 2026-10-14 | Dawid Karczewski (mieszkaniec), rejestr ulic PRG (GUGiK) | Ulica Kukułek przeniesiona: usunięty odcinek dorysowany na prywatnym terenie przy Lipowej i Kaczora Donalda; Kukułek to odcinek od Lipowej do Rumcajsa (w OSM opisany jako Margarytki). |
| 2026-10-14 | GESUT (obraz WMS starostwa garwolińskiego) | 2 możliwe hydranty „do weryfikacji”: dwa małe włazy „w” obok siebie na odgałęzieniu wodociągu, tak jak przy hydrantach ze zgłoszeń nr 3 i 4 (skrypt `hydranty_wlazy.py`; wcześniejsze 30 punktów zawężone po uwagach Dawida). |
