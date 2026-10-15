# Historia zmian mapy

Każda poprawka danych na mapie ma tu wiersz: skąd się wzięła (numer uwagi z arkusza „Uwagi do mapy Osiedla Wilga” albo inne źródło) i co zmieniono. Ten sam numer jest w opisie commita (`Uwaga nr 12: …`), więc `git log -- data/` pokazuje dokładne różnice w danych.

| Data | Źródło | Co zmieniono |
| --- | --- | --- |
| 2026-10-12 | Dawid Karczewski (mieszkaniec) | Dodany adres Lipowa 12 (dawna Pierogarnia Aniołowa i sklep): nie ma go w rejestrze PRG, położenie z OpenStreetMap. |
| 2026-10-14 | Uwaga nr 3 | Hydrant przy Trakcie Słonecznym (C7), przy znaku drogowym: w GESUT wpisany jako dwa włazy, naniesiony w miejscu drugiego włazu od przewodu. |
| 2026-10-14 | Uwaga nr 4 | Hydrant przy Trakcie Słonecznym (C6), naprzeciwko „Żubra”: w GESUT wpisany jako dwa włazy, naniesiony w miejscu drugiego włazu od przewodu. |
| 2026-10-14 | Dawid Karczewski (mieszkaniec), rejestr ulic PRG (GUGiK) | Ulica Kukułek przeniesiona: usunięty odcinek dorysowany na prywatnym terenie przy Lipowej i Kaczora Donalda; Kukułek to odcinek od Lipowej do Rumcajsa (w OSM opisany jako Margarytki). |
| 2026-10-14 | GESUT (obraz WMS starostwa garwolińskiego) | 2 możliwe hydranty „do weryfikacji”: dwa małe włazy „w” obok siebie na odgałęzieniu wodociągu, tak jak przy hydrantach ze zgłoszeń nr 3 i 4 (skrypt `hydranty_wlazy.py`; wcześniejsze 30 punktów zawężone po uwagach Dawida). |
| 2026-10-14 | Uwagi nr 5, 8, 9, 10 | Hydranty potwierdzone w terenie: Leśników (B3), Aleja Cicha (F3), Szyszkowa (F3) zmienione z „do sprawdzenia” na potwierdzone; nowy hydrant przy Alei Cichej 1 (F3), którego nie ma na mapie sieci. |
| 2026-10-14 | Uwaga nr 7 | Hydrant przy Miłej (F3) nie znaleziony w terenie: przeniesiony do „do sprawdzenia”. |
| 2026-10-14 | Uwaga nr 16 | Dodane 16 adresów na terenie osiedla, które w rejestrze PRG należą do miejscowości Skurcza (adres bez ulicy, np. Skurcza 60), także w wyszukiwarce i indeksie jako „Skurcza (adres bez ulicy)”. |
| 2026-10-15 | Uwagi nr 24, 33 | Margarytki przy działkach 1300 i 1351 (D4): odcinek ukośny przecina ogrodzona działka. Od Pionierów zostaje krótki dojazd do działki 1300, dalej do zakrętu tylko dojście piesze wzdłuż drzew; od południa Margarytki kończy się na granicy działki 1351, skąd dojazd w prawo wzdłuż działki do domu nr 29. Przebieg według rysunku Dawida na geoportalu. |
| 2026-10-15 | Uwagi nr 24, 33 (poprawka) | Margarytki przy działkach 1300 i 1351 przerysowana dokładnie według rysunku Dawida na geoportalu (zrzut dopasowany do punktów adresowych): wjazd od Pionierów z łukiem, przerwa przy ogrodzeniu, dojście piesze, dojazd do nr 29; południowy odcinek do Wakacyjnej wzdłuż działki drogowej 2669 (wcześniej przekoszony). |
