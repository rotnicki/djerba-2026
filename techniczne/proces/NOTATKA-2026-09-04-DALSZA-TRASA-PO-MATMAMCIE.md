# Dalsza trasa po Matmacie – wstępna analiza materiałów z 4 września 2026

Status: robocza analiza techniczna na podstawie aktualnego kompletu materiałów na Google Drive. Obecny stan folderu traktowany jest jako najprawdopodobniej pełny komplet materiałów z 4 września, ale sam Google Drive nie pozwala potwierdzić, czy proces wysyłania z iPhone'a został formalnie zakończony.

## Stan kompletności materiału

Sekwencja materiałów z 4 września sięga co najmniej `IMG_1875`. Bezpośredni listing potwierdził obecność całej sekwencji `IMG_1854–1868`, w tym `IMG_1860.MOV` i `IMG_1861.PNG`. W tym zakresie nie ma luk numeracji. Fizycznych duplikatów na etapie analizy nie usuwamy.

## Ustalona relacja uczestnika – powrót z Matmaty

Po ostatnim punkcie w rejonie Matmaty przewodnik zapowiedział zasadniczo bezpośrednią drogę powrotną do hotelu. Według pamięci Mikołaja pozostawało ponad 170 km i ponad dwie godziny jazdy. Rozważano jeszcze postój w miejscu odwiedzonym rano, ale z niego zrezygnowano. Kierowca na dłuższych odcinkach jechał szybko; Mikołaj mierzył prędkość telefonem. Późniejsza seria zdjęć miała dokumentować ponowny dojazd do El Kantara z intensywnym blaskiem niskiego słońca.

## Etap kontrolny 1 – pomiar prędkości

`IMG_1861.PNG` to zrzut aplikacji GPS Speed: **108 km/h**, średnia **89 km/h**, maksimum **108 km/h**, kierunek **E**, wysokość 114 m, dokładność GPS 4,6 m. Potwierdza relację o prędkości około 110 km/h.

## Etap kontrolny 2 – koniec postoju i pierwsza dalsza kotwica

- `IMG_1854` – 14:52:55, około 33.55285 N, 9.97195 E;
- `IMG_1855` – 14:52:57, praktycznie ten sam punkt;
- `IMG_1856` – 14:54:44, nadal ten sam punkt;
- `IMG_1860.MOV` – 15:42:20, GPS 33.6022 N, 10.2051 E, długość około 7,07 s.

Około 47,5 minuty między końcem postoju a `IMG_1860` jest zgodne z ciągłą jazdą.

## Etap kontrolny 3 – `IMG_1860.MOV`: autostrada A1

Film `IMG_1860.MOV` został porównany z lokalnym OSM `tunisia-260822.osm.pbf`. Punkt GPS leży około 8 m od dwóch nitek oznaczonych `highway=motorway`, `ref=A1`, `int_ref=TAH 1`. OSM podaje `maxspeed=110`, `minspeed=60`, `lanes=2`, `oneway=yes`. Wizualnie film również pokazuje rozdzieloną drogę szybkiego ruchu.

Wniosek: o **15:42:20** autokar jechał **A1 / TAH 1**.

## Etap kontrolny 4 – `IMG_1862`: RR117

- czas: **16:54:24**;
- GPS około **33.62693 N, 10.94785 E**;
- duży błąd GPS, około 174 m;
- obraz z jadącego pojazdu: droga, drzewa, niska zabudowa, niskie słońce;
- punkt wypada w korytarzu **RR117 / Route Romaine Djerba–Zarzis / Chaussée Romaine**.

Wniosek: około 16:54 grupa wróciła już do osi RR117 prowadzącej ku El Kantara. Nie utożsamiamy jeszcze tego zdjęcia z właściwą groblą nad wodą.

## Etap kontrolny 5 – `IMG_1863`: pierwsze ujęcie wody i blasku

- czas: **16:55:23**;
- GPS około **33.62670 N, 10.94928 E**;
- `GPSHPositioningError` około **332 m**, więc lokalizacja tylko orientacyjna;
- zdjęcie wykonane przez szybę jadącego pojazdu;
- widać rozległą wodę i bardzo silny blask niskiego słońca odbijającego się od jej powierzchni oraz element infrastruktury drogowej przy dolnej krawędzi;
- wykonane 59 sekund po `IMG_1862`.

To pierwsze ujęcie odpowiadające wspomnieniu o „drodze ku słońcu”.

## Etap kontrolny 6 – `IMG_1864`: potwierdzenie przejazdu bezpośrednio przy wodzie

`IMG_1864.HEIC` sprawdzono jako osobny mikrokrok.

- czas wykonania: **16:55:25**, zaledwie **2 sekundy po `IMG_1863`**;
- GPS około **33.62830 N, 10.94551 E**;
- zapisany `GPSHPositioningError` około **9,38 m**, a więc zdecydowanie lepszy niż w `IMG_1863`;
- zdjęcie wykonane przez szybę autokaru;
- kadr przedstawia otwartą wodę, bardzo silne odbicie słońca oraz barierę/element konstrukcji drogi na pierwszym planie;
- para `IMG_1863–1864` jednoznacznie dokumentuje jazdę drogą biegnącą bezpośrednio przez lub wzdłuż akwenu w rejonie El Kantara.

Wniosek: **16:55:23–16:55:25** to już właściwa seria przejazdu przy wodzie związana z powrotem przez El Kantara / Chaussée Romaine. `IMG_1864` jest znacznie lepszą kotwicą GPS niż `IMG_1863`.

## Etap kontrolny 7 – `IMG_1865`: dalszy przejazd tym samym odcinkiem

`IMG_1865.HEIC` sprawdzono jako kolejny osobny mikrokrok.

- czas wykonania: **16:55:39**;
- GPS około **33.629825 N, 10.943542 E**;
- zapisany `GPSHPositioningError` około **4,75 m**, czyli bardzo dobra dokładność;
- plik powstał **14 sekund po `IMG_1864`**;
- pozycja przesuwa się dalej na północny zachód względem `IMG_1864`, zgodnie z ciągłym przejazdem tym samym korytarzem drogowym przy wodzie.

Wniosek: `IMG_1864–1865` tworzą dwie bardzo dobre kotwice GPS w odstępie 14 sekund i potwierdzają ciągłość przejazdu przez odcinek El Kantara / Route Romaine. Przy końcowym zestawieniu z OSM należy użyć przede wszystkim tych dwóch punktów, a `IMG_1863` traktować pomocniczo ze względu na jego duży błąd GPS.

## Robocza sekwencja powrotu

**Matmata → ostatni punkt panoramiczny do około 14:55 → szybki przejazd bez postoju → 15:42 A1 / TAH 1 → pomiar 108 km/h → 16:54 RR117 → 16:55:23–16:55:39 przejazd bezpośrednio przy wodzie w rejonie El Kantara, z intensywnym blaskiem słońca → dalszy wjazd na Dżerbę → Club Palm Azur przed 19:08.**

## Następny mikrokrok

Sprawdzić wyłącznie `IMG_1866`, zapisać wynik i dopiero potem przejść do `IMG_1867`.