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
| 2026-10-15 | Uwagi nr 20, 21, 26 | Biedronki i Jemiołuszki (C7): z „nieprzejezdna” na żółtą (wąska, ale przejezdna); potwierdziły to niezależnie dwie osoby i Dawid. |
| 2026-10-15 | Uwaga nr 28 | Nowe miejsce do zawracania przy Sosnowej (E7), wskazane przez Dawida. |
| 2026-10-15 | Uwaga nr 31, Dawid Karczewski (mieszkaniec) | Hydrant przy Jemiołuszkach (C7) potwierdzony w terenie (wygląda na zniszczony, w QGIS uwaga o niepewnej sprawności); usunięty hydrant z mapy sieci na działce 519/4, którego nie ma w terenie. Dymek i legenda: „sprawdzony w terenie (stoi), nie sprawdzano, czy działa”, bo działania żadnego hydrantu nie sprawdzano. |
| 2026-10-15 | Uwaga nr 25 | Chrząszcza (C5): usunięty odcinek na zachód od Traktu Słonecznego (w terenie go nie ma); po stronie wschodniej tylko dojazd do działki 1080, bez połączenia z Poziomkową (sprawdzone przez Dawida w terenie). |
| 2026-10-15 | Uwaga nr 30 | hydrant przy Trakcie Słonecznym (C7) potwierdzony w terenie |
| 2026-10-15 | Uwaga nr 32 | dodany brakujący hydrant przy Trakcie Słonecznym (C6) |
| 2026-10-15 | Uwaga nr 29 | usunięty hydrant na działkach prywatnych przy Jodłowej (D6), pozostałość po dawnym ośrodku |
| 2026-10-15 | Uwaga nr 35 | Ośrodek Wypoczynkowo-Szkoleniowy „Wilga”, Saperów 1A: punkt charakterystyczny i adres (brak w PRG) |
| 2026-10-15 | Uwaga nr 27 | Chrobotka: wąska; krótki odcinek przy Drozdów nieprzejezdny dla dużego wozu |
| 2026-10-15 | Uwaga nr 18 | Ostrówek (A2): usunięta nieistniejąca droga; dorysowane dojazdy do 7A i do 11A–11E |
| 2026-10-15 | Uwaga nr 17 | Pionierów przejezdna dla lekkiego wozu, z wyjątkiem skarpy przy Drodze Księżycowej i odcinka do Miłej (do potwierdzenia w terenie) |
| 2026-10-15 | Dawid Karczewski (mieszkaniec) | Punkty charakterystyczne: Ośrodek Wypoczynkowy ZZ Pracowników Cywilnych MSWiA (nieczynny), Brzozowa 1, 1A, 1B (D6; wg katalogu firm i.pl), oraz Ośrodek Socjoterapeutyczny „Wspólny Dom”, Plac Myśliwski 1 (C7). |
| 2026-10-15 | opencaching.pl (skrzynki OP880B, OP2C20) | Brzozowa 1, 1A, 1B to dawny ośrodek MSW (skrzynka „Ośrodek MSW” na działce 1926), nazwa punktu poprawiona. Nowy punkt: opuszczony ośrodek Z.U.D. przy Bolka i Lolka (D5, działka 1920/1). |
| 2026-10-16 | Uwagi nr 11, 12 | Jodłowa i Al. Słońca (D4/E4): zgłoszenie „nieprzejezdna dla ciężkiego sprzętu” nie potwierdziło się, Dawid przejechał obie ulice bez problemu. Kolory bez zmian (Al. Słońca zielona, Jodłowa żółta, węższa); dopisana weryfikacja w terenie. |
| 2026-10-16 | Uwaga nr 36 | Babie Lato (C3) na zielono na całej długości; miejsce do zawracania przy skrzyżowaniu z Sikorek. |
| 2026-10-16 | Uwagi nr 37, 13 | Usunięty nieistniejący odcinek (ok. 115 m) między skrzyżowaniem Rajskiej a Sarenek (C2). |
| 2026-10-16 | Uwagi nr 38, 39 | Bobrów (D1): łuk wzdłuż posesji usunięty, został dojazd do nr 6; nowy dojazd na północ do polany nad Wilgą (trochę zarośnięty) z miejscem do zawracania i punktem poboru wody z rzeki. |
| 2026-10-16 | Uwaga nr 40 | Usunięta wschodnia część drogi przez działki prywatne między pętlą Bobrowa a łukiem (D2). |
| 2026-10-16 | Uwaga nr 41 | Odcinek przy adresach Za Jałowcami 5–30 przemianowany z „Bobrów” na „Za Jałowcami” (zgodnie z PRG). |
| 2026-10-16 | Uwagi nr 43, 46, 47 | Krasnali za końcem tylko pieszo; Zielony Zaułek na czerwono (za wąsko dla samochodu); dojście piesze Leśnych Ludzi – Przebiśniegów (E3). |
| 2026-10-16 | Uwagi nr 48, 19 | Dorysowany odcinek Muminków od Przebiśniegów do Garwolinki, przejezdny samochodem (E3). |
| 2026-10-16 | Uwaga nr 49 | Usunięty zdublowany obrys budynku przy Garwolince 1. |
| 2026-10-16 | Uwaga nr 50 | Pionierów od Raroga na wschód na czerwono: przechył boczny ok. 10% (G4). |
| 2026-10-16 | Uwagi nr 52, 53 | Wakacyjna na zielono od zachodu do Spokojnej; miejsca do zawracania przy Szyszkowej i przy Konwaliowej. |
| 2026-10-16 | Uwaga nr 42 | Usunięta nieistniejąca ulica bez nazwy od Rumcajsa na wschód (E2) wraz ze stromiznami; dodana kręta droga leśna od Rumcajsa do północnego końca Al. Słońca (przebieg wg BDOT10k), żółta, do sprawdzenia. |
| 2026-10-16 | Uwagi nr 44, 45 | Leśnych Ludzi (E3) kończy się dojazdem do działki; dalej ścieżka wzdłuż podziału działek do końca Krasnali; odcinek do Zielonego Zaułka i zachodni kawałek Zielonego Zaułka tylko quadem lub pieszo (wg BDOT10k i Dawida w terenie). |
| 2026-10-16 | Uwaga nr 51 | Usunięta Śnieżki między Wakacyjną a Bolka i Lolka (G5/H4), w terenie jej nie ma; dodane ścieżki z końca Wakacyjnej, w tym na północ do końca Pionierów (wg BDOT10k, potwierdzone przez Dawida). |
| 2026-10-16 | Uwaga nr 39 (uzupełnienie) | Bobrów (D1/D2): półokrąg wzdłuż posesji usunięty w całości, w terenie są tylko dojazdy do posesji; dodany prawdziwy przebieg Bobrowa, droga gruntowa na zewnątrz półokręgu (wg BDOT10k i geoportalu); dojazd do polany nad Wilgą i do nr 6 podpięte do niej. |
| 2026-10-16 | Uwaga nr 37 (uzupełnienie) | Dorysowane przejezdne przedłużenie Rajskiej od Sarenek łukiem do drogi wzdłuż działek (C2); droga przy stanicy poprowadzona łukiem zamiast dwóch prostych odcinków (przebieg wg BDOT10k, wskazany przez Dawida). |
| 2026-10-16 | Dawid Karczewski (mieszkaniec), BDOT10k | Ostrówek (A2/B2) jako jedna ciągła żółta droga od drogi 801 do skrzyżowania z Rajską (przebieg wg BDOT10k, zastąpił trzy odcinki bez nazwy); Puszczyka (B3) poprawiona wg BDOT10k, dochodzi do Sikorek. |
| 2026-10-16 | Dawid Karczewski (mieszkaniec), BDOT10k, PRG | Nowy Żabieniec w kolumnach G i H siatki (las osiągalny od osiedla, wyjątek jak Skurcza): drogi wg BDOT10k przycięte do granicy siatki (Żabieniecka asfaltowa na zielono, drogi gruntowe na żółto do sprawdzenia), 9 brakujących budynków, 69 adresów PRG (Żabieniecka, Nad Łąkami, Przy Lesie) z dopiskiem miejscowości w wyszukiwarce i indeksie. |
| 2026-10-16 | Uwagi nr 54, 55 | Żabieniecka 10 (Nowy Żabieniec, G3): adres wg PRG przy najbardziej północnym budynku; prywatna droga utwardzona 4,5 m od Żabienieckiej na zielono, miejsce do zawracania przy budynku (zweryfikowane przez Dawida). |
| 2026-10-16 | Uwaga nr 56 | Krótka droga przy Muminków (G3) na czerwono: zawalona krzakami i gałęziami, tylko pieszo. |
| 2026-10-17 | Uwagi nr 57, 58 | Czerwonego Kapturka (G6) na zielono: przejezdna dla ciężkiego wozu; Limby (H6) od Czerwonego Kapturka do Śnieżki na czerwono: nieprzejezdna (sprawdzone w terenie przez Dawida). |
| 2026-10-17 | Uwagi nr 59–62 | Nad Łąkami (G3/H3, Nowy Żabieniec): droga na zielono od wschodu do zakrętu przy uwadze nr 61; dwa hydranty z mapy sieci potwierdzone w terenie (nr 62 pomalowany na niebiesko); kapliczka dodana do miejsc charakterystycznych. |
| 2026-10-17 | Uwaga nr 63 | Cyganówka 70 (za Wilgą od strony osiedla, ok. 200 m na północ od G1): dojazd od brukowanej drogi leśnej (przedłużenie Garwolinki) na żółto, przebieg wg BDOT10k i cieniowania NMT, do sprawdzenia w terenie (szlaban LP); adres w wyszukiwarce i indeksie z dopiskiem „dojazd tylko od Garwolinki, nie od DK76”. |
| 2026-10-17 | Uwaga nr 15 | Saperów (C7/C8) na zielono od Traktu Słonecznego do Ośrodka Wypoczynkowo-Szkoleniowego „Wilga” (Saperów 1A), potwierdził Dawid. |
| 2026-10-17 | Uwaga nr 63 (uzupełnienie) | Dwa budynki przy Cyganówce 70: lewy wg BDOT10k, prawy (nr 70) odrysowany z ewidencji budynków na geoportalu; ostatni odcinek dojazdu poprowadzony wzdłuż skarpy do budynku nr 70. |
| 2026-10-17 | Uwaga nr 63 (potwierdzenie) | Mieszkaniec Cyganówki 70 potwierdził dojazd: z brukowanej drogi leśnej skosem w lewo; opis drogi uzupełniony. |
| 2026-10-19 | Uwagi nr 57, 58 (cofnięte) | Czerwonego Kapturka (G6) i Limby (H6) wróciły na żółto: zgłoszenia były niepodpisane i bez „Zasadna?” = TAK, naniesione omyłkowo 17.10; czekają na sprawdzenie w terenie. |
| 2026-10-19 | Atlas A3 | Adres mapa-osiedle-wilga.goliat.dev i kod QR do wersji cyfrowej na stronie przeglądowej i na każdym arkuszu. |
| 2026-10-19 | Uwagi nr 65–68 | Wakacyjna (H4): zamiast uskoku i ścieżki prosta droga jako przedłużenie Wakacyjnej do zakrętu przy górce, dalej droga nad łąkami do drogi przy zboczu (wg BDOT10k), obie na żółto, sprawdzone w terenie; objazd dookoła górki i skrót pod górkę od ścieżki do Wakacyjnej (przebieg wg cieniowania NMT); usunięty skrót, którego w terenie nie ma (nr 67). |
| 2026-10-19 | Uwagi nr 71, 72 | Śnieżki (H5) od Czterech Wiatrów do Bolka i Lolka na żółto; wschodni odcinek Limby (H5) do Bolka i Lolka usunięty, w terenie go nie ma. |
| 2026-10-19 | Uwagi nr 75, 76 (i 57, 58) | Czerwonego Kapturka (G6) od Gajowej do Limby na zielono (sprawdził Dawid); Limby na odcinku z uwagi nr 58 zostaje żółta, przejezdna mimo krzaków. |
| 2026-10-19 | Uwagi nr 78, 79 | Poziomkowa (D) i cała Al. Huberta (B6–C6) na zielono, sprawdził Dawid. |
| 2026-10-19 | Uwagi nr 64, 77 | Szlaban Nadleśnictwa Garwolin przy Bobrowie (F2) w miejscach charakterystycznych; miejsce do zawracania przy Gajowej (F5). |
| 2026-10-19 | Uwagi nr 69, 70, 73, 80 | Adresy: Śnieżki 20 przesunięty na budynek, Śnieżki 3 (tabliczka na bramie) i Czeremchy 1M dodane; nowy budynek bez numeru przy Bolka i Lolka (G5), obrys przybliżony z cieniowania NMT. |
| 2026-10-19 | Uwagi nr 72, 74 (uzupełnienie) | Limby (H5): dojazd do Bolka i Lolka 52 od Limby, dawne połączenie z Bolka i Lolka na czerwono (przerwane przez posesję nr 54, przebieg wg BDOT10k); Limby (G6): przechył boczny 5–10° w opisie drogi. |
