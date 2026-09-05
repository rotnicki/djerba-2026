# Rekonstrukcja kotwic El Kantara – 4 września 2026

Status: robocza rekonstrukcja geometrii przejazdu na podstawie najlepszych kotwic GPS i lokalnego pliku OSM `tunisia-260822.osm.pbf`.

## Mikrokrok 1 – `IMG_1864`

- czas zdjęcia: **16:55:25**;
- GPS zdjęcia: około **33.62830 N, 10.94551 E**;
- deklarowany błąd GPS zdjęcia: około **9,38 m**;
- najbliższa droga w lokalnym OSM: **Route Romaine Djerba - Zarzis**;
- `ref=RR117`, `alt_name=Chaussée Romaine`, `highway=secondary`, `surface=asphalt`;
- odległość punktu GPS od geometrii drogi: około **3,8 m**.

Wniosek: o 16:55:25 autokar znajdował się bezpośrednio na osi RR117.

## Mikrokrok 2 – `IMG_1865`

- czas zdjęcia: **16:55:39**;
- GPS zdjęcia: około **33.629825 N, 10.943542 E**;
- deklarowany błąd GPS: około **4,75 m**;
- odległość od tej samej geometrii RR117: około **1,3 m**.

Wniosek: druga bardzo mocna kotwica ciągłego przejazdu RR117.

## Mikrokrok 3 – `IMG_1867`

- czas zdjęcia: **16:58:51**;
- GPS zdjęcia: około **33.66223 N, 10.92280 E**;
- deklarowany błąd GPS: około **10,58 m**;
- linia brzegowa OSM przebiega około **1,0 m** od punktu;
- równoległa droga w budowie około **14,4 m** od punktu;
- czynna RR117 około **24,8 m** od punktu;
- czynna RR117 zachowuje ciągłość przez odcinki OSM `198577348 → 198577347 (bridge=yes) → 31360290`.

Wniosek: `IMG_1867` wiążemy z czynną RR117, nie z równoległą drogą w budowie.

## Mikrokrok 4 – połączenie `IMG_1865 → IMG_1867`

Ciągłe geometrie czynnej RR117 `198577348`, `198577347` i `31360290` zostały połączone w jedną linię i użyte do projekcji obu kotwic na oś drogi.

- czas między zdjęciami: **3 min 12 s = 192 s**;
- długość odcinka RR117 pomiędzy rzutami obu punktów na oś drogi: około **4,103 km**;
- wynikająca średnia prędkość na tym odcinku: około **76,9 km/h**;
- wartość jest fizycznie spójna z ciągłą jazdą autokarem drogą regionalną i nie wymaga żadnego skrótu, postoju ani przejazdu drogą w budowie.

Wniosek: kotwice `IMG_1865` i `IMG_1867` można spójnie połączyć **jednym ciągłym przejazdem czynną RR117 / Route Romaine / Chaussée Romaine**. Około 4,1 km w 3 min 12 s daje średnio około 77 km/h, co dodatkowo wzmacnia rekonstrukcję.

## Następny krok

Zamknąć serię `IMG_1862–1868` jednym końcowym wnioskiem, rozdzielając mocne kotwice GPS od zdjęć pomocniczych o dużym błędzie lokalizacji.