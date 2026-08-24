# Dżerba i południe Tunezji — specyfikacja, wdrożenie i odtwarzanie mapy

Status: **pierwsza wersja wdrożona 24 sierpnia 2026 r. w `wycieczki.md`**.

Korekta po ocenie użytkownika: usunięto kolizje etykiet Toujane i Matmaty z numerowanymi punktami, przeniesiono znaczniki nad warstwę napisów oraz ujednolicono obie legendy map. Nazwy własne w legendzie są podawane w mianowniku, a po myślniku następuje krótka etykieta opisowa zgodna z Atlasem.

Mapa jest drugim poziomem orientacji przestrzennej w Atlasie miejsc. Uzupełnia szczegółową mapę Dżerby, ale nie jest jej wstawką ani powiększeniem.

Pliki wdrożenia:

- generator `techniczne/mapy/generate_south_tunisia_map.py`;
- wynik `_includes/maps/south-tunisia.svg`;
- osadzenie i tekstowy odpowiednik w `wycieczki.md`;
- wspólne style w `assets/css/style.css`;
- zamrożone źródło opisane w `snapshot-osm-tunezja.md`.

## Cel i miejsce publikacji

Mapa ma pokazywać uczestnikom:

- gdzie na Dżerbie znajduje się hotel będący punktem startowym;
- w którą stronę wyjeżdża się przez Groblę El Kantara;
- jak układają się względem siebie główne miejsca na kontynencie;
- jak duża jest różnica skali między wyjazdem w okolice Medenine lub Tataouine a programem prowadzącym do Tozeur i Chebiki.

Mapa jest osadzona w `wycieczki.md` w sekcji `## Atlas miejsc`, bezpośrednio po nagłówku `### Wyjazd z Dżerby na kontynent` i przed opisem El Kantary. To miejsce rozpoczyna przejście od szczegółowego poziomu wyspy do poziomu południowej Tunezji.

Mapa nie pokazuje tras konkretnych organizatorów. Linie drogowe są wyłącznie uproszczoną warstwą orientacyjną.

## Inwentaryzacja miejsc

Pierwsza wersja obejmuje wszystkie miejsca mające własny nagłówek w kontynentalnej części Atlasu oraz dwa doprecyzowania występujące w jego treści: Zaafrane przy Douz i Chebikę przy Tozeur. Hotel pozostaje punktem odniesienia także na mapie regionalnej.

| Oznaczenie | Miejsce | Obiekt w snapshotcie OSM | Sposób przedstawienia |
| --- | --- | --- | --- |
| H | Club Palm Azur | węzeł `1123865146` | hotel i punkt startowy, romb |
| 1 | Grobla El Kantara | węzeł `6616525005` | kierunek wyjazdu z wyspy |
| 2 | Medenine | węzeł `287585326` | miasto |
| 3 | Tataouine | węzeł `264885332` | miasto |
| 4 | Chenini | węzeł `297760994` | miejscowość |
| 5 | Ksar Hadada | droga/powierzchnia `215111919` | środek geometrii zabytku `tourism=attraction`, `historic=ruins` |
| 6 | Ksar Ouled Soltane | relacja `2516832` | środek geometrii atrakcji |
| 7 | Toujane | węzeł `1997328129` | miejscowość |
| 8 | Matmata i Hotel Sidi Idriss | węzeł `559400323` | wspólny punkt przy hotelu, ponieważ obiekt jest częścią opisu Matmaty |
| 9 | Ksar Ghilane | węzeł `264887592` | oaza/miejscowość |
| 10 | Douz i Zaafrane | węzeł Douz `264881676` | wspólne oznaczenie kierunku; Zaafrane leży blisko Douz |
| bez numeru | Chott el-Jerid | relacja `3969167` | rzeczywisty wieloczęściowy obszar, nie pinezka |
| 11 | Tozeur | węzeł `298018887` | miasto |
| 12 | Chebika | węzeł atrakcji `6853346685` | górska oaza/atrakcja |

Tamerza i Midès są wymienione zbiorczo w opisie okolic Tozeur, ale nie mają własnych części Atlasu ani osobnych punktów na pierwszej mapie. Ich dodanie zwiększałoby zagęszczenie północno-zachodniego narożnika bez proporcjonalnej korzyści na tym etapie.

## Zakres i parametry

Ramka danych:

- zachód: `7.80°E`;
- wschód: `11.15°E`;
- południe: `32.70°N`;
- północ: `34.42°N`.

Zakres obejmuje pełny układ od Dżerby i hotelu do Chebiki, z marginesem wokół skrajnych punktów. Zachowuje też cały potrzebny fragment Chott el-Jerid. Nie obejmuje północnej Tunezji ani obszarów leżących dalej na południe od punktów opisanych w Atlasie.

Parametry SVG:

- `viewBox`: `0 0 1000 660`;
- układ poziomy;
- lokalne odwzorowanie equirektangularne ze skalowaniem długości geograficznej przez cosinus średniej szerokości geograficznej;
- uproszczenie lądu i dróg: `0.0012°` z zachowaniem topologii;
- uproszczenie Chott el-Jerid: `0.003°` z zachowaniem topologii;
- drogi: klasy OSM `trunk`, `primary` i `secondary`, po połączeniu odcinków i odrzuceniu fragmentów krótszych niż `0.012°`;
- podziałka liniowa: `0–100 km`, z punktem pośrednim `50 km`;
- strzałka północy w prawym górnym rogu.

Na mapie celowo pominięto budynki, drogi lokalne, granice administracyjne, ukształtowanie terenu, przypadkowe POI i przebiegi ofert wycieczkowych.

## Dane i geometria

Źródło:

- plik `tunisia-260822.osm.pbf`;
- SHA-256 `4629c6f40e1749f266fa339ba484f473414cbb026c7b6267a47f16715266bfaf`;
- dane OpenStreetMap z dystrybucji Geofabrik.

Generator odtwarza z danych OSM:

- linię brzegową kontynentu;
- Dżerbę i większe wyspy w ramce;
- wybrane drogi główne;
- geometrię Chott el-Jerid z relacji wielokątowej;
- współrzędne wszystkich znaczników.

Kontur lądu nie jest ręcznie rysowany. Szerszy margines odczytu danych jest konieczny, aby linia brzegowa dochodziła do fizycznych krawędzi płótna i prawidłowo oddzielała Zatokę Gabès od lądu.

## Dostępność i osadzenie

Mapa jest osadzona inline przez Jekyll:

```liquid
{% include maps/south-tunisia.svg %}
```

SVG jest atomową grafiką:

- ma `role="img"`;
- `aria-labelledby` wskazuje unikatowe `title` i `desc`;
- `desc` objaśnia H, numery 1–12, obszar Chott el-Jerid oraz podziałkę;
- wewnętrzne warstwy są ukryte przed osobną nawigacją czytnika ekranu;
- bezpośrednio po mapie znajduje się zwykły tekst HTML z pełnym przypisaniem oznaczeń, krótkimi etykietami objaśniającymi charakter miejsc, kierunkami i orientacyjnymi odległościami w linii prostej;
- nazwy własne w legendzie pozostają w mianowniku, dzięki czemu każdy punkt działa jako samodzielna nazwa, a nie fragment zdania zależny od tekstu poprzedzającego listę.

Hotel odróżnia się rombem i literą H. Atrakcje mają koła i numery. Chott el-Jerid ma własny obrys kreskowany, więc nie zależy wyłącznie od koloru.

Kontener mapy jest nazwanym regionem i może otrzymać fokus. Na małych ekranach szeroka mapa zachowuje minimalną szerokość `48rem` i może być przewijana poziomo. Tekstowy odpowiednik nie wymaga obsługi SVG.

## Kolory i motywy

Mapa korzysta ze wspólnych semantycznych tokenów map w `assets/css/style.css`. Dodatkowy token `--map-salt-lake` określa powierzchnię Chott el-Jerid.

Wariant ciemny jest uruchamiany przez `@media (prefers-color-scheme: dark)`. Wymuszone kolory korzystają z wartości systemowych. Etykiety mapy regionalnej mają obrys w kolorze lądu, dzięki czemu pozostają czytelne na drogach bez tworzenia osobnych pól tekstowych.

## Odtworzenie

Środowisko i wersje zależności są wspólne z mapą Dżerby:

```bash
python -m venv .venv-map
.venv-map/bin/pip install \
  -r techniczne/mapy/requirements-djerba-map.txt
```

Przed generowaniem trzeba potwierdzić sumę snapshotu zgodnie z `snapshot-osm-tunezja.md`.

```bash
.venv-map/bin/python \
  techniczne/mapy/generate_south_tunisia_map.py \
  /ścieżka/do/tunisia-260822.osm.pbf \
  _includes/maps/south-tunisia.svg
```

Po zmianie punktów lub zakresu trzeba równocześnie zaktualizować generator, `desc`, listę i opis pod mapą oraz tę dokumentację.

## Kontrole pierwszej wersji

Wymagane kontrole przed publikacją:

1. zgodność SHA-256 snapshotu;
2. obecność wszystkich skonfigurowanych obiektów OSM;
3. deterministyczność ponownego generowania;
4. poprawność XML i unikatowość identyfikatorów;
5. brak kolizji etykiet ze znacznikami oraz czytelność numerów; znaczniki są renderowane nad napisami jako dodatkowe zabezpieczenie;
6. render w trybie jasnym i ciemnym;
7. czytelność Chott el-Jerid jako obszaru;
8. obecność podziałki i strzałki północy;
9. zgodność listy HTML z numerami SVG;
10. wynikowy render strony i publikacja GitHub Pages;
11. późniejszy ręczny test VoiceOver na urządzeniu użytkownika.
