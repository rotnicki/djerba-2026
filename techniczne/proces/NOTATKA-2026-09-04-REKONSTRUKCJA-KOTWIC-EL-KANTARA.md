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

Wniosek: `IMG_1864` jest bardzo mocną kotwicą potwierdzającą, że o 16:55:25 autokar znajdował się bezpośrednio na osi **RR117 / Route Romaine Djerba–Zarzis / Chaussée Romaine**. Zgodność GPS z geometrią OSM jest bardzo wysoka i mieści się wyraźnie w deklarowanym błędzie pomiaru zdjęcia.

## Mikrokrok 2 – `IMG_1865`

- czas zdjęcia: **16:55:39**;
- GPS zdjęcia: około **33.629825 N, 10.943542 E**;
- deklarowany błąd GPS zdjęcia: około **4,75 m**;
- najbliższa droga w lokalnym OSM jest tym samym obiektem co dla `IMG_1864`: **Route Romaine Djerba - Zarzis**, OSM ID `198577348`;
- `ref=RR117`, `alt_name=Chaussée Romaine`, `highway=secondary`, `surface=asphalt`;
- odległość punktu GPS od geometrii RR117 wynosi tylko około **1,3 m**.

Wniosek: `IMG_1865` jest jeszcze mocniejszą kotwicą niż `IMG_1864`. Dwa zdjęcia wykonane w odstępie 14 sekund leżą odpowiednio około 3,8 m i 1,3 m od **tej samej geometrii OSM RR117 / Chaussée Romaine**. Potwierdza to ciągły przejazd autokaru tą drogą, a nie przypadkowe sąsiedztwo osi drogowej.

## Mikrokrok 3 – `IMG_1867`

- czas zdjęcia: **16:58:51**;
- GPS zdjęcia: około **33.66223 N, 10.92280 E**;
- deklarowany błąd GPS: około **10,58 m**;
- najbliższą linią dowolnego typu w lokalnym OSM jest `natural=coastline`, w odległości około **1,0 m** od punktu;
- po ograniczeniu analizy do obiektów drogowych najbliższa geometria leży około **14,4 m** od punktu;
- jest oznaczona `highway=construction`, `construction=primary`, `oneway=yes`, OSM ID `1326350355`;
- odległość około 14,4 m jest nieco większa od deklarowanego błędu GPS zdjęcia 10,58 m, dlatego tego dopasowania nie należy traktować tak jednoznacznie jak `IMG_1864–1865`;
- jednocześnie położenie niemal dokładnie na geometrii linii brzegowej jest zgodne z obrazem zdjęcia: akwen, łódź i bariera/konstrukcja przy drodze.

Wniosek: `IMG_1867` potwierdza przestrzennie dojście serii do strefy linii brzegowej, ale lokalny OSM przedstawia w tym miejscu bardziej złożoną sytuację niż przy `1864–1865`: linia brzegowa przebiega praktycznie przez punkt GPS, a najbliższa geometria drogowa jest oznaczona jako odcinek drogi głównej w budowie. Nie wolno jeszcze utożsamiać tej geometrii w budowie z faktycznie używaną jezdnią bez sprawdzenia sąsiednich obiektów OSM i ciągłości RR117.

## Stan po trzech kotwicach

- `IMG_1864` i `IMG_1865` bardzo mocno i bezpośrednio potwierdzają **RR117 / Chaussée Romaine**;
- `IMG_1867`, 3 min 12 s po `IMG_1865`, znajduje się już praktycznie na odwzorowanej linii brzegowej i przy bardziej złożonym układzie drogowym;
- wizualna ciągłość zdjęć oraz kierunek przemieszczania wskazują na przejazd południowym połączeniem Dżerby, ale dokładny przebieg pomiędzy `1865` i `1867` wymaga teraz analizy ciągłości geometrii OSM.

## Następny mikrokrok

Sprawdzić wyłącznie sąsiednie geometrie drogowe wokół `IMG_1867` i ustalić, gdzie w lokalnym OSM biegnie w tym miejscu przejezdna RR117 / Route Romaine. Wynik zapisać przed łączeniem `IMG_1865 → IMG_1867` w jeden przebieg.