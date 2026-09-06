# Dalsza trasa po Matmacie – analiza materiałów z 4 września 2026

Status: **analiza drogi powrotnej zakończona na poziomie technicznej rekonstrukcji możliwej z dostępnych materiałów**. Podstawa: zdjęcia i filmy z 4 września, ich metadane, relacja uczestnika oraz lokalny OSM `tunisia-260822.osm.pbf`.

## Stan kompletności materiału

Sekwencja materiałów z 4 września sięga co najmniej `IMG_1875`. Bezpośredni listing potwierdził obecność całej sekwencji `IMG_1854–1868`, w tym `IMG_1860.MOV` i `IMG_1861.PNG`. W tym zakresie nie ma luk numeracji. Fizycznych duplikatów na etapie analizy nie usuwamy.

## Ustalona relacja uczestnika – powrót z Matmaty

Po ostatnim punkcie w rejonie Matmaty przewodnik zapowiedział zasadniczo bezpośrednią drogę powrotną do hotelu. Według pamięci Mikołaja pozostawało ponad 170 km i ponad dwie godziny jazdy. Rozważano jeszcze postój w miejscu odwiedzonym rano, ale z niego zrezygnowano. Kierowca na dłuższych odcinkach jechał szybko; Mikołaj mierzył prędkość telefonem. Późniejsza seria zdjęć dokumentuje ponowny dojazd do El Kantara z intensywnym blaskiem niskiego słońca.

Mikołaj podaje z pamięci, że **powrót autokaru do Club Palm Azur nastąpił około 17:15**. Tę godzinę zapisujemy jako **relację uczestnika**, a nie czas wyprowadzony z metadanych zdjęcia. Jest ona spójna z ostatnią mocną kotwicą fotograficzną przy El Kantara o 17:00:21 i oznacza, że zdjęcie hotelowe `IMG_1869.HEIC` z 19:08:15 nie dokumentuje chwili powrotu, lecz dopiero późniejszy pobyt w hotelu.

## Koniec pobytu w Matmacie

- `IMG_1854` – 14:52:55, około 33.55285 N, 9.97195 E;
- `IMG_1855` – 14:52:57, praktycznie ten sam punkt;
- `IMG_1856` – 14:54:44, nadal ten sam punkt.

Wniosek: ostatni postój panoramiczny trwał co najmniej do **14:54:44**; wyjazd nastąpił około 14:55 lub chwilę później.

## Matmata → A1

`IMG_1860.MOV`:

- czas: **15:42:20**;
- GPS: **33.6022 N, 10.2051 E**;
- wizualnie: rozdzielona droga szybkiego ruchu;
- lokalny OSM: punkt leży około 8 m od jezdni oznaczonych `highway=motorway`, `ref=A1`, `int_ref=TAH 1`;
- OSM podaje m.in. `maxspeed=110`, `minspeed=60`, `lanes=2`, `oneway=yes`.

Dodatkowa rekonstrukcja grafowa lokalnego OSM dla odcinka od ostatniego punktu w Matmacie do kotwicy `IMG_1860` wskazuje najkrótszy spójny ciąg drogowy przez **RR107 → A1**.

- długość po sieci: około **58,5 km**;
- czas od `IMG_1856` 14:54:44 do `IMG_1860` 15:42:20: **47 min 36 s**;
- średnia dla całego odcinka: około **73,8 km/h**.

Wynik jest czasowo i drogowo bardzo wiarygodny. Dlatego powrót z rejonu Matmaty do punktu `IMG_1860` można z wysokim prawdopodobieństwem rekonstruować jako **RR107 → A1 / TAH1**.

## Pomiar prędkości

`IMG_1861.PNG` to zrzut aplikacji GPS Speed:

- prędkość bieżąca: **108 km/h**;
- średnia: **89 km/h**;
- maksimum: **108 km/h**;
- kierunek: **E**;
- dokładność GPS: **4,6 m**.

Potwierdza to relację o szybkiej jeździe na długim odcinku i dobrze współgra z limitem `110 km/h` zapisanym w OSM dla A1. Nie przypisujemy zrzutu do dokładnie tego samego punktu co `IMG_1860`, bo PNG nie daje pewnego czasu wykonania.

## A1 → RR117

Kolejna twarda kotwica to `IMG_1862`:

- czas: **16:54:24**;
- GPS około **33.62693 N, 10.94785 E**;
- błąd GPS około 174 m;
- lokalny OSM sytuuję punkt w korytarzu **RR117 / Route Romaine Djerba–Zarzis / Chaussée Romaine**.

Między kotwicą A1 a RR117 upływa **1 h 12 min 04 s**.

Lokalny graf OSM nie daje w tej chwili jednego bezbłędnie połączonego przebiegu w całym odcinku A1 → RR117: pomiędzy dwiema dużymi składowymi sieci pozostaje około **1,89 km luki topologicznej w danych OSM**. Nie należy zatem sztucznie dopisywać konkretnej ulicy lub łącznika tylko po to, aby zamknąć graf.

Pewne jest natomiast:

- o 15:42:20 autokar był na A1 / TAH1;
- o 16:54:24 był już w korytarzu RR117 przed El Kantara;
- przejazd między tymi punktami był ciągły i czasowo zgodny z relacją o bezpośrednim powrocie bez planowanego dodatkowego postoju.

Dokładny mikroprzebieg A1 → RR117 pozostaje więc **rekonstrukcją wysokiego poziomu, a nie pewnym śladem co do każdej ulicy**.

## RR117 / El Kantara – seria `IMG_1862–1868`

Szczegółowa rekonstrukcja tego odcinka została zakończona w osobnej notatce `NOTATKA-2026-09-04-REKONSTRUKCJA-KOTWIC-EL-KANTARA.md`.

Najważniejsze ustalenia:

- `IMG_1863`, 16:55:23 – pierwsze ujęcie rozległej wody i intensywnego blasku niskiego słońca;
- `IMG_1864`, 16:55:25 – około **3,8 m** od osi RR117;
- `IMG_1865`, 16:55:39 – około **1,3 m** od tej samej RR117;
- `IMG_1866`, 16:58:45 – nadal akwen i infrastruktura drogowa, ale GPS bardzo niedokładny;
- `IMG_1867`, 16:58:51 – dobra kotwica w strefie linii brzegowej; czynna RR117 biegnie około **24,8 m** od punktu, równolegle do odcinka drogi w budowie;
- `IMG_1868`, 17:00:21 – ostatnie ujęcie wodnej serii, z łodziami blisko drogi.

Czynna RR117 zachowuje ciągłość OSM przez odcinki `198577348 → 198577347 (bridge=yes) → 31360290`.

Dla `IMG_1865 → IMG_1867`:

- czas: **3 min 12 s**;
- odległość po czynnej RR117: około **4,103 km**;
- średnia prędkość: około **76,9 km/h**.

Wniosek: seria `IMG_1862–1868` dokumentuje **ciągły przejazd na Dżerbę RR117 / Route Romaine Djerba–Zarzis / Chaussée Romaine przez południowe połączenie wyspy w rejonie El Kantara**. Nie ma podstaw, by przyjmować przejazd równoległą drogą w budowie.

## Dalszy przejazd na wyspie i powrót do hotelu

Po serii wodnej brak kolejnej mocnej kotwicy zdjęciowej aż do hotelu. Pierwszy pewny późniejszy materiał hotelowy:

- `IMG_1869.HEIC` – **19:08:15**, GPS około **33.76292 N, 11.02089 E**, wejście do `DOLCE VITA RESTAURANT` w Club Palm Azur.

Nie jest to jednak godzina powrotu z wycieczki. Zgodnie z relacją Mikołaja autokar wrócił do Club Palm Azur **około 17:15**. Ostatnia kotwica przy El Kantara o 17:00:21 jest z takim wspomnieniem czasowo spójna. Dokładności co do pojedynczych minut nie należy wyprowadzać ze zdjęć; `17:15` pozostaje godziną orientacyjną podaną przez uczestnika.

## Końcowa rekonstrukcja drogi powrotnej

Najlepiej udokumentowany przebieg to:

**ostatni punkt panoramiczny w Matmacie do co najmniej 14:54:44 → wyjazd około 14:55 → RR107 → A1 / TAH1 → 15:42:20 pewna kotwica na A1 → szybka jazda, pomiar do 108 km/h → przejazd w kierunku Dżerby bez potwierdzonego postoju → 16:54:24 korytarz RR117 → 16:55–17:00 seria przejazdu przez wodny odcinek El Kantara / Chaussée Romaine → dalszy przejazd przez Dżerbę → według relacji Mikołaja powrót do Club Palm Azur około 17:15.**

### Poziomy pewności

- **bardzo wysoka**: koniec postoju w Matmacie, kotwica A1, RR117/El Kantara oraz późniejsza obecność w hotelu o 19:08;
- **wysoka**: Matmata → RR107 → A1, ciągły przejazd RR117 przez El Kantara;
- **relacja uczestnika**: powrót do Club Palm Azur około **17:15**;
- **średnia**: dokładny przebieg między A1 a pierwszą kotwicą RR117, ponieważ lokalny graf OSM ma około 1,89 km luki topologicznej;
- **nieustalona na podstawie samych metadanych**: dokładna minuta przyjazdu do hotelu i każdy kilometr trasy na Dżerbie po 17:00, bo brak kolejnych kotwic zdjęciowych.

## Status

**Techniczna analiza drogi powrotnej z Matmaty do hotelu jest zakończona.** Następnym etapem nie jest już dalsze szukanie trasy, lecz włączenie ustalonej chronologii i miejsc do właściwego wpisu dziennika podróży z 4 września 2026.