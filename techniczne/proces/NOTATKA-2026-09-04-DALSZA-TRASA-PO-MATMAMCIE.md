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

- czas: **16:55:25**;
- GPS około **33.62830 N, 10.94551 E**;
- `GPSHPositioningError` około **9,38 m**;
- przez szybę autokaru widać otwartą wodę, silne odbicie słońca oraz barierę/konstrukcję drogi.

Wniosek: `IMG_1864` jest dobrą kotwicą GPS właściwej serii przejazdu przy wodzie w rejonie El Kantara.

## Etap kontrolny 7 – `IMG_1865`: dalszy przejazd tym samym odcinkiem

- czas: **16:55:39**;
- GPS około **33.629825 N, 10.943542 E**;
- `GPSHPositioningError` około **4,75 m**;
- 14 sekund po `IMG_1864` pozycja przesuwa się dalej zgodnie z ciągłym przejazdem.

Wniosek: `IMG_1864–1865` tworzą dwie bardzo dobre kotwice GPS.

## Etap kontrolny 8 – `IMG_1866`: dalsze ujęcie akwenu, ale GPS o bardzo małej wartości precyzyjnej

`IMG_1866.HEIC` sprawdzono jako kolejny osobny mikrokrok.

- czas wykonania: **16:58:45**;
- zapisany GPS około **33.65542 N, 10.92629 E**;
- `GPSHPositioningError` wynosi aż około **1236 m**, więc tego punktu nie wolno używać do dokładnego przypisania drogi;
- wizualnie zdjęcie przedstawia nadal **rozległy akwen**, niskie słońce częściowo przesłonięte chmurami i bardzo jasne odbicie na wodzie;
- na pierwszym planie wyraźnie widać **metalową barierę / rurową konstrukcję przy drodze**, co potwierdza wykonywanie zdjęcia z jadącego pojazdu na odcinku bezpośrednio przy wodzie;
- zdjęcie wykonano **3 min 06 s po `IMG_1865`**.

Wniosek: obraz `IMG_1866` potwierdza, że kilka minut po serii `1863–1865` autokar nadal znajdował się w wodnym krajobrazie związanym z przejazdem El Kantara / południowym wjazdem na Dżerbę. Natomiast jego własna współrzędna GPS ma ponad kilometrową deklarowaną niepewność, dlatego w rekonstrukcji geometrii należy opierać się przede wszystkim na `IMG_1864–1865`, a `IMG_1866` wykorzystywać jako dowód wizualno-czasowy.

## Etap kontrolny 9 – `IMG_1867`: dobra kotwica GPS kilka sekund później

`IMG_1867.HEIC` sprawdzono jako osobny mikrokrok.

- czas wykonania: **16:58:51**;
- GPS około **33.66223 N, 10.92280 E**;
- `GPSHPositioningError` około **10,58 m**, czyli ponownie dobra dokładność;
- zdjęcie wykonano **6 sekund po `IMG_1866`**;
- wizualnie widać rozległy akwen, niskie słońce prześwitujące przez chmury i szeroki pas odbicia na wodzie;
- na pierwszym planie widoczna jest masywna metalowa bariera/rurowa konstrukcja przy drodze, a po prawej mała łódź na wodzie;
- obraz jednoznacznie potwierdza dalszą jazdę drogą bezpośrednio przy akwenie.

Wniosek: `IMG_1867` jest znacznie lepszą kotwicą przestrzenną niż `IMG_1866` i pokazuje, że o **16:58:51** grupa nadal znajdowała się na wodnym odcinku południowego wjazdu na Dżerbę. Przy składaniu geometrii przejazdu należy wykorzystać `IMG_1864`, `1865` i `1867` jako główne punkty o dobrej dokładności GPS, a `1863` i `1866` traktować pomocniczo.

## Etap kontrolny 10 – `IMG_1868`: ostatnie ujęcie serii przy wodzie

`IMG_1868.HEIC` sprawdzono jako osobny mikrokrok.

- czas wykonania: **17:00:21**;
- zapisany GPS około **33.66728 N, 10.92084 E**;
- `GPSHPositioningError` wynosi około **1575 m**, więc współrzędna ma bardzo małą wartość do dokładnego wyznaczania drogi;
- wizualnie widać nadal **szeroki akwen**, niskie słońce przesłonięte częściowo chmurami i wyraźne promienie oraz odbicie na wodzie;
- na pierwszym planie znajduje się masywna bariera/rurowa konstrukcja przy drodze;
- bardzo dobrze widoczna jest **mała łódź zacumowana blisko drogi**, a po prawej fragment drugiej łodzi;
- zdjęcie wykonano **1 min 30 s po `IMG_1867`**.

Wniosek: `IMG_1868` zamyka serię zdjęć wodnego odcinka powrotu. Obrazowo bardzo dobrze potwierdza dalszy przejazd wzdłuż akwenu i charakter infrastruktury przy drodze, ale własny GPS jest zbyt niedokładny, aby używać go jako głównej kotwicy przestrzennej. Do precyzyjnej rekonstrukcji geometrii serii `1862–1868` należy opierać się głównie na `IMG_1864`, `IMG_1865` i `IMG_1867`.

## Robocza sekwencja powrotu

**Matmata → ostatni punkt panoramiczny do około 14:55 → szybki przejazd bez postoju → 15:42 A1 / TAH 1 → pomiar 108 km/h → 16:54 RR117 → 16:55:23–16:55:39 seria dobrych kotwic przejazdu przy wodzie w rejonie El Kantara → 16:58:45–17:00:21 dalsze ujęcia akwenu i infrastruktury drogowej, z których `IMG_1867` ma dobrą dokładność GPS → dalszy wjazd na Dżerbę → Club Palm Azur przed 19:08.**

## Następny mikrokrok

Zestawić wyłącznie trzy najlepsze kotwice `IMG_1864`, `IMG_1865` i `IMG_1867` z lokalnym OSM i zapisać wynik przed próbą odtworzenia pełnego przebiegu `IMG_1862–1868`.