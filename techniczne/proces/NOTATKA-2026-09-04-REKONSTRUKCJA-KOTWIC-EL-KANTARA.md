# Rekonstrukcja kotwic El Kantara – 4 września 2026

Status: robocza rekonstrukcja geometrii przejazdu na podstawie najlepszych kotwic GPS i lokalnego pliku OSM `tunisia-260822.osm.pbf`.

## Mikrokrok 1 – `IMG_1864`

- czas zdjęcia: **16:55:25**;
- GPS zdjęcia: około **33.62830 N, 10.94551 E**;
- deklarowany błąd GPS zdjęcia: około **9,38 m**;
- najbliższa droga w lokalnym OSM: **Route Romaine Djerba - Zarzis**;
- `ref=RR117`;
- `alt_name=Chaussée Romaine`;
- `highway=secondary`;
- `surface=asphalt`;
- odległość punktu GPS od geometrii tej drogi w projekcji UTM: około **3,8 m**.

Wniosek: `IMG_1864` jest bardzo mocną kotwicą potwierdzającą, że o 16:55:25 autokar znajdował się bezpośrednio na osi **RR117 / Route Romaine Djerba–Zarzis / Chaussée Romaine**.

## Mikrokrok 2 – `IMG_1865`

- czas zdjęcia: **16:55:39**;
- GPS zdjęcia: około **33.629825 N, 10.943542 E**;
- deklarowany błąd GPS zdjęcia: około **4,75 m**;
- najbliższa droga w lokalnym OSM jest tym samym obiektem co dla `IMG_1864`: **Route Romaine Djerba - Zarzis**, OSM ID `198577348`;
- `ref=RR117`, `alt_name=Chaussée Romaine`, `highway=secondary`, `surface=asphalt`;
- odległość punktu GPS od geometrii RR117 wynosi tylko około **1,3 m**.

Wniosek: `IMG_1865` jest jeszcze mocniejszą kotwicą niż `IMG_1864` i potwierdza ciągły przejazd tą samą RR117.

## Mikrokrok 3 – `IMG_1867`

- czas zdjęcia: **16:58:51**;
- GPS zdjęcia: około **33.66223 N, 10.92280 E**;
- deklarowany błąd GPS: około **10,58 m**;
- najbliższą linią dowolnego typu w lokalnym OSM jest `natural=coastline`, około **1,0 m** od punktu;
- najbliższy obiekt drogowy to odcinek `highway=construction`, `construction=primary`, około **14,4 m** od punktu;
- czynna **RR117 / Route Romaine / Chaussée Romaine** biegnie jednak równolegle w tym samym korytarzu i znajduje się około **24,8 m** od punktu `IMG_1867`;
- czynny odcinek ma `highway=secondary`, `ref=RR117`, `surface=asphalt`, `oneway=no`;
- geometria czynnej RR117 łączy się ciągle z wcześniejszym odcinkiem OSM `198577348` przez krótki mostowy segment `198577347` (`bridge=yes`) i dalej przez odcinek `31360290`.

Wniosek: nie ma podstaw, by uznawać, że autokar jechał drogą w budowie. Lokalny OSM zawiera równoległą geometrię nowego odcinka w budowie, ale **czynna RR117 nadal tworzy ciągłą, przejezdną oś drogową dokładnie w tym samym korytarzu**. `IMG_1867` należy więc wiązać z przejazdem czynną RR117, z przesunięciem GPS około 24,8 m względem osi drogi, co jest większe od deklarowanego błędu pojedynczego pomiaru, ale pozostaje zgodne z ciągłością trasy, obrazem brzegu i sąsiednim układem OSM.

## Punkt kontrolny – rozstrzygnięcie sąsiedztwa `IMG_1867`

Niejasność dotycząca `IMG_1867` została rozstrzygnięta: obok czynnej RR117 biegnie równoległy obiekt oznaczony jako droga w budowie. Do rekonstrukcji przejazdu należy używać **czynnej RR117**, a geometrię budowy traktować jako obiekt sąsiedni, nie trasę autokaru.

## Następny krok

Połączyć `IMG_1865 → IMG_1867` po ciągłej geometrii czynnej RR117 i policzyć długość oraz średnią prędkość między kotwicami.