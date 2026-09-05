# Dalsza trasa po Matmacie – wstępna analiza materiałów z 4 września 2026

Status: robocza analiza techniczna na podstawie aktualnego kompletu materiałów na Google Drive. Obecny stan folderu traktowany jest jako najprawdopodobniej pełny komplet materiałów z 4 września, ale sam Google Drive nie pozwala potwierdzić, czy proces wysyłania z iPhone'a został formalnie zakończony.

## Stan kompletności materiału

Wcześniejsze luki `IMG_1798`, `IMG_1807` i `IMG_1808` zostały wypełnione. Sekwencja po `IMG_1810` sięga co najmniej `IMG_1875`. W folderze występują fizyczne duplikaty; na etapie analizy nie są usuwane.

Ponowny bezpośredni listing folderu 5 września potwierdził obecność całej sekwencji `IMG_1854–1868`, w tym `IMG_1860.MOV` i `IMG_1861.PNG`. W tym zakresie nie ma luk numeracji.

## Ustalona relacja uczestnika – powrót z Matmaty

Po opuszczeniu ostatniego punktu w rejonie Matmaty – najprawdopodobniej postoju panoramicznego dokumentowanego około 14:52 – przewodnik zapowiedział już zasadniczo bezpośrednią drogę powrotną do hotelu. Według pamięci Mikołaja:

- do hotelu pozostawało ponad 170 km;
- przejazd miał trwać ponad dwie godziny;
- kierowca na dłuższych odcinkach jechał bardzo szybko; Mikołaj mierzył jego prędkość telefonem;
- rozważano jeszcze postój w miejscu, w którym grupa była również rano – prawdopodobnie przy restauracji lub podobnym obiekcie – ale przewodnik, pilot i kierowca ostatecznie z niego zrezygnowali, uznając, że trasę można przejechać jednym ciągiem;
- podczas długiej drogi powrotnej wykonano niewiele zdjęć;
- późniejsza seria powinna dokumentować ponowny dojazd w rejon El Kantara / grobli rzymskiej, z niskim słońcem i intensywnym blaskiem przed pojazdem.

## Etap kontrolny 1 – zachowany pomiar prędkości

`IMG_1861.PNG` został sprawdzony wizualnie. Jest to zrzut ekranu aplikacji **GPS Speed** wykonany podczas jazdy powrotnej. Na ekranie widnieje:

- aktualna prędkość: **108 km/h**;
- średnia: **89 km/h**;
- maksimum: **108 km/h**;
- kierunek: **E** (wschód);
- wysokość: **114 m**;
- dokładność GPS: **4,6 m**;
- jednostka: km/h.

To jest bezpośrednie źródłowe potwierdzenie wcześniejszej relacji Mikołaja, że kierowca na dłuższych odcinkach dochodził do około 110 km/h.

## Etap kontrolny 2 – koniec postoju i pierwsza dalsza kotwica GPS

Dodatkowo odczytano właściwe metadane EXIF/QuickTime z plików po punkcie panoramicznym:

- `IMG_1854.HEIC` – **14:52:55**, GPS około **33.55285 N, 9.97195 E**, dokładność pozioma około 4,75 m; nadal praktycznie punkt panoramiczny;
- `IMG_1855.HEIC` – **14:52:57**, GPS około **33.55284 N, 9.97194 E**, dokładność około 4,15 m; nadal ten sam punkt;
- `IMG_1856.HEIC` – **14:54:44**, GPS około **33.55286 N, 9.97202 E**, dokładność około 6,8 m; nadal bez istotnego przemieszczenia, więc grupa była jeszcze przy końcu postoju lub dopiero ruszała;
- `IMG_1860.MOV` – czas lokalny z metadanych QuickTime **15:42:20**, czas UTC w kontenerze 14:42:21Z; GPS **33.6022 N, 10.2051 E**, wysokość około 93 m, dokładność pozioma około 10,2 m; długość filmu około 7,07 s.

To tworzy pierwszą bardzo mocną parę kotwic dla drogi powrotnej:

**około 14:55 – ostatni materiał w praktycznie nieruchomym punkcie panoramicznym w Matmacie → 15:42 – pojazd jest już przy 33.6022 N, 10.2051 E, daleko na wschód od Matmaty.**

Odstęp wynosi około 47,5 minuty. Jest zgodny z relacją o bezpośredniej szybkiej jeździe bez postoju.

`IMG_1861.PNG` występuje chronologicznie bezpośrednio po `IMG_1860.MOV` w bibliotece, więc pomiar 108 km/h najprawdopodobniej należy do tego samego odcinka jazdy lub bezpośrednio kolejnego fragmentu. Dokładnego czasu PNG nie należy jednak zgadywać, ponieważ zrzut nie niesie równoważnego EXIF czasu wykonania.

## Etap kontrolny 3 – identyfikacja drogi na `IMG_1860.MOV`

Film `IMG_1860.MOV` został sprawdzony wizualnie i porównany z lokalnym plikiem OSM `tunisia-260822.osm.pbf`.

- kadr pokazuje jazdę szeroką, rozdzieloną barierami drogą szybkiego ruchu przez płaski, bardzo suchy teren;
- punkt GPS filmu: **33.6022 N, 10.2051 E**;
- najbliższe dwie nitki drogi w lokalnym OSM leżą około **7,7–8,2 m** od punktu GPS;
- obie są oznaczone jako `highway=motorway`, `ref=A1`, `int_ref=TAH 1`;
- OSM podaje dla tego odcinka `maxspeed=110`, `minspeed=60`, `lanes=2`, `oneway=yes`; na jednej z nitek także `surface=asphalt`;
- zgodność GPS, obrazu i geometrii jest bardzo wysoka.

Wniosek: o **15:42:20** autokar jechał **autostradą A1 / Trans-African Highway 1**, a nie zwykłą drogą regionalną. To jest pierwszy dokładnie zidentyfikowany odcinek drogi powrotnej po Matmacie.

Wartość `maxspeed=110` z OSM jest dodatkowo zgodna z wykonanym chwilę później pomiarem 108 km/h, ale nie należy z tego automatycznie wnioskować, że zrzut `IMG_1861.PNG` wykonano dokładnie w tym samym miejscu.

## Etap kontrolny 4 – `IMG_1862.HEIC`: ponowny dojazd do Route Romaine / RR117

`IMG_1862.HEIC` został pobrany bezpośrednio z Dysku, odczytany i porównany z lokalnym OSM.

- czas wykonania: **16:54:24**;
- EXIF GPS: około **33.62693 N, 10.94785 E**;
- zapisany `GPSHPositioningError` wynosi około **174 m**, więc samej współrzędnej nie należy traktować z dokładnością do pojedynczych metrów;
- wizualnie zdjęcie jest wykonane z jadącego pojazdu: widać asfaltową drogę, krawężnik/chodnik, drzewa, niską zabudowę i linie energetyczne; słońce jest już wyraźnie nisko;
- mimo dużego deklarowanego błędu GPS punkt wypada w korytarzu `RR117`;
- najbliższy odcinek OSM to **Route Romaine Djerba - Zarzis**, `ref=RR117`, `alt_name=Chaussée Romaine`, `highway=secondary`, `surface=asphalt`, około **8,8 m** od zapisanej współrzędnej;
- w bezpośrednim sąsiedztwie są również odcinki `RR117` związane z układem jezdni/ronda.

Wniosek o wysokiej wiarygodności: o **16:54:24** grupa była już ponownie na **RR117 / Route Romaine Djerba–Zarzis**, czyli w korytarzu prowadzącym do historycznej grobli El Kantara. To jest pierwszy twardy punkt potwierdzający powrót do tej samej osi komunikacyjnej, którą grupa opuszczała Dżerbę rano.

Nie należy jeszcze twierdzić, że `IMG_1862` przedstawia sam właściwy odcinek grobli nad wodą. Dokładne przejście przez El Kantara trzeba ustalić z `IMG_1863–1868`.

## Pierwsze ustalone punkty po Dar Taoufik Matmata

### około 14:29–14:40 – Hotel Sidi Driss / plan zdjęciowy „Gwiezdnych wojen” w Matmacie

- `IMG_1811.HEIC` – 14:29:03, GPS około 33.54417 N, 9.96783 E;
- `IMG_1820.HEIC` – 14:34:40, GPS około 33.54261 N, 9.96706 E;
- `IMG_1830.HEIC` – 14:37:01, GPS około 33.54254 N, 9.96700 E;
- `IMG_1840.HEIC` – 14:40:08, GPS około 33.54258 N, 9.96705 E.

Seria dokumentuje Hotel Sidi Driss w Matmacie i dekoracje związane z „Gwiezdnymi wojnami”.

### około 14:52–14:55 – krótki postój panoramiczny na północ od centrum Matmaty

- `IMG_1850.HEIC` – 14:52:35, GPS około 33.55285 N, 9.97193 E;
- `IMG_1853.HEIC` – 14:52:51, praktycznie ten sam punkt;
- `IMG_1854–1856` potwierdzają pozostawanie w tym samym miejscu co najmniej do 14:54:44;
- zdjęcia pokazują suchy, silnie urzeźbiony i tarasowy krajobraz wzgórz wokół Matmaty.

Na obecnym etapie jest to najbardziej prawdopodobny ostatni postój przed długim przejazdem powrotnym.

## Powrót w stronę Dżerby – następne kotwice

- `IMG_1860.MOV` – 15:42:20, GPS 33.6022 N, 10.2051 E, **autostrada A1 / TAH 1**;
- `IMG_1861.PNG` – pomiar GPS Speed: 108 km/h, średnia 89 km/h, kierunek E;
- `IMG_1862.HEIC` – 16:54:24, GPS około 33.62693 N, 10.94785 E, **RR117 / Route Romaine Djerba–Zarzis**.

Pomiędzy 15:42 a 16:54 następuje dalszy wyraźny ruch na wschód: od A1 aż do korytarza RR117 prowadzącego ku El Kantara.

## Powrót do hotelu i wieczór

- `IMG_1869.HEIC` – 19:08:15, GPS około 33.76292 N, 11.02089 E; Club Palm Azur;
- `IMG_1874.HEIC` – 19:41:29, GPS około 33.76331 N, 11.02108 E; kolacja;
- `IMG_1875.HEIC` – 20:00:30, GPS około 33.76304 N, 11.02082 E; deser.

## Robocza sekwencja po 14:20

**Dar Taoufik Matmata → Hotel Sidi Driss około 14:29–14:40 → punkt panoramiczny około 14:52–14:55 → bezpośredni długi przejazd powrotny → 15:42 autostrada A1 / TAH 1 przy 33.6022 N, 10.2051 E → pomiar GPS Speed 108 km/h, kierunek E → 16:54 RR117 / Route Romaine Djerba–Zarzis → właściwy przejazd El Kantara do ustalenia z kolejnych zdjęć → Club Palm Azur przed 19:08 → kolacja i deser.**

## Następny etap kontrolny

1. sprawdzić `IMG_1863` i zapisać wynik;
2. następnie kolejno `IMG_1864`, `1865`, `1866`, `1867`, `1868`, zapisując po każdym istotnym ustaleniu;
3. znaleźć dokładny moment przejazdu przez El Kantara / groblę rzymską;
4. dopiero potem złożyć ciąg dróg Matmata → A1 → RR117 → El Kantara.