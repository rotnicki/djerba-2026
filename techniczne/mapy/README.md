# Mapy — dane źródłowe

Mapy przygotowywane dla przewodnika mają być oparte na rzeczywistych danych OpenStreetMap, a nie na grafikach generowanych przez AI.

Ten dokument dotyczy technicznej strony map. Ogólny plan materiałów wizualnych, w tym zdjęć reprezentujących miejsca w `wycieczki.md`, znajduje się w `techniczne/wizualizacje/README.md`.

## Cel map

Planowane mapy mają przede wszystkim pomagać w orientacji przestrzennej: pokazywać położenie ważnych miejsc, relacje między nimi oraz — tam, gdzie ma to sens — przebieg tras wycieczek.

Nie mają zastępować map nawigacyjnych ani tekstowego opisu. Mają być uproszczone i czytelne, również dla osób słabowidzących i widzących przewodników.

## Źródło danych

Źródło: Geofabrik — wycinek danych OpenStreetMap dla Tunezji.

Geofabrik nie definiuje osobnych subregionów dla Tunezji. Do przygotowania map Dżerby i południowej Tunezji należy więc pobrać snapshot całego kraju, a następnie wyciąć lub przefiltrować potrzebny obszar lokalnie.

Manifest techniczny pobranego snapshotu znajduje się w pliku `techniczne/mapy/snapshot-osm-tunezja.md`.

Pliki źródłowe mają być przechowywane jako zamrożony snapshot z konkretną datą, tak aby możliwe było późniejsze odtworzenie map z tych samych danych.

## Archiwum plików źródłowych

Google Drive: folder `Dżerba 2026/Mapy – dane źródłowe`

https://drive.google.com/drive/folders/1WJh1QCaqH3ZNnX5Nks2TPib11TDDdwqN

Zapisany snapshot: [tunisia-260822.osm.pbf na Google Drive](https://drive.google.com/file/d/1MZYSe-eAzNul0wcBEsQ9WWMpBdWtRNov/view?usp=drivesdk)

W manifeście snapshotu zapisano:

- nazwę pliku;
- datę pobrania;
- adres źródłowy;
- format;
- rozmiar;
- sumę SHA-256.

Do publicznego repozytorium trafiają przede wszystkim końcowe, lekkie pliki map, np. SVG, a nie pełna baza danych OSM.

## Planowany sposób przygotowania

Roboczy proces:

1. pobranie konkretnego, datowanego snapshotu danych Tunezji z Geofabrik;
2. zachowanie tego pliku w archiwum na Google Drive;
3. wybór potrzebnego obszaru, np. całej Dżerby albo trasy prowadzącej na południe Tunezji;
4. wybór tylko potrzebnych warstw danych, np. lądu, wybrzeża, głównych dróg, miejscowości i punktów opisanych w przewodniku;
5. świadome pominięcie zbędnych szczegółów, np. wszystkich budynków, lokalnych uliczek i przypadkowych punktów POI;
6. wyrenderowanie uproszczonej mapy, docelowo przede wszystkim jako SVG;
7. umieszczenie przy mapie wymaganej atrybucji `© OpenStreetMap contributors`;
8. sprawdzenie czytelności i użyteczności przed powieleniem wzorca.

## Pierwsze wdrożenie: mapa Dżerby

Pierwsza uproszczona mapa została przygotowana dla sekcji `Atlas miejsc` w pliku `wycieczki.md`. Obejmuje całą Dżerbę i pokazuje:

- hotel Club Palm Azur jako punkt odniesienia;
- Houmt Souk i fort Borj Ghazi Mustapha;
- Erriadh i Djerbahood;
- synagogę El Ghriba;
- Guellalę;
- Djerba Explore;
- Ras Rmel;
- pomocniczo Midoun i El Kantarę;
- zarys wyspy oraz wybrane drogi główne.

Kod źródłowy SVG znajduje się w `_includes/maps/djerba.svg`. Jekyll wstawia go bezpośrednio do HTML strony przez `{% raw %}{% include maps/djerba.svg %}{% endraw %}`. Dzięki temu kolory mapy mogą korzystać ze zmiennych CSS strony, a jej nazwa i opis są dostępne w tym samym drzewie dostępności co pozostała treść.

Mapa jest generowana przez skrypt `techniczne/mapy/generate_djerba_map.py` z zamrożonego snapshotu `tunisia-260822.osm.pbf`. Skrypt wymaga pakietów Python `osmium` i `shapely`. Przykładowe uruchomienie z katalogu głównego repozytorium:

```bash
python techniczne/mapy/generate_djerba_map.py \
  /ścieżka/do/tunisia-260822.osm.pbf \
  _includes/maps/djerba.svg
```

Skrypt odtwarza z danych OSM linię brzegową, wybiera drogi klasy `primary` i `secondary`, usuwa krótkie fragmenty nieczytelne w skali całej wyspy i umieszcza skonfigurowane punkty z Atlasu. Wygenerowany SVG zapisuje w metadanych nazwę oraz sumę SHA-256 snapshotu.

### Dostępność pierwszej mapy

SVG jest traktowany jako jedna grafika o roli `img`, z nazwą w elemencie `title` i krótkim opisem w `desc`. Wewnętrzne warstwy mapy są ukryte przed czytnikiem ekranu, ponieważ ich surowa kolejność nie przekazuje użytecznej relacji przestrzennej.

Bezpośrednio pod mapą znajduje się zwykły tekst HTML zawierający:

- przypisanie litery i numerów do nazw miejsc;
- położenie hotelu jako punktu odniesienia;
- kierunki i przybliżone odległości w linii prostej;
- informację o grupach blisko położonych miejsc;
- wyjaśnienie kierunku wyjazdu przez El Kantarę.

Kolor nie jest jedynym sposobem rozróżnienia punktów: hotel ma romb i literę `H`, a atrakcje mają koła i numery. Na małym ekranie mapa zachowuje czytelną wielkość etykiet i może być przewijana poziomo; opis tekstowy pozostaje dostępny bez przewijania grafiki.

Style w `assets/css/style.css` definiują oddzielne semantyczne kolory mapy dla trybu jasnego, `prefers-color-scheme: dark` oraz trybu wymuszonych kolorów. Kontrast sprawdzono osobno dla etykiet, dróg, obrysu wyspy i znaczników.

## Roboczy zasięg pierwszej mapy szerszego obszaru

Pierwsza mapa szerszego obszaru dla `wycieczki.md` ma roboczo pokazywać skalę wyjazdów z Dżerby na południe Tunezji. Jej funkcją jest orientacja decyzyjna: gdzie leży Dżerba, w którą stronę prowadzą główne kierunki wycieczek i jak daleko od wyspy znajdują się miejsca opisywane w przewodniku.

Robocza nazwa mapy:

`Dżerba i południe Tunezji — orientacyjna mapa wycieczek`

Zakres planistyczny, do weryfikacji po pobraniu danych i pierwszym próbnym renderze:

- zachód: około `7.85°E`;
- wschód: około `11.12°E`;
- południe: około `32.70°N`;
- północ: około `34.40°N`.

Zakres powinien objąć co najmniej:

- Dżerbę jako punkt startu wycieczek;
- El Kantara / groblę z Dżerby na kontynent;
- Medenine;
- Tataouine;
- Chenini;
- Ksar Hadada;
- Ksar Ouled Soltane;
- Toujane;
- Matmatę i Hotel Sidi Idriss;
- Ksar Ghilane;
- Douz / Zaafrane;
- Chott el-Jerid jako obszar orientacyjny, nie pojedynczą pinezkę;
- Tozeur i Chebikę jako najdalszy zachodni kierunek części programów dwudniowych.

Ta mapa nie ma szczegółowo pokazywać wszystkich punktów na samej Dżerbie. Punkty wyspiarskie, takie jak Houmt Souk, Djerbahood, El Ghriba, Guellala, Djerba Explore, Ras Rmel i hotel Club Palm Azur, powinny zostać pokazane na osobnej mapie Dżerby.

Podany zakres nie jest jeszcze ostateczną ramką produkcyjną. Po próbnym renderze trzeba sprawdzić czytelność etykiet, marginesy, zagęszczenie punktów i ewentualnie skorygować granice mapy bez zmiany jej funkcji.

## Styl, kolorystyka i tryb ciemny

OpenStreetMap traktujemy jako źródło danych, a nie jako obowiązkowy wzór kolorystyczny. Nie kopiujemy automatycznie wyglądu standardowych kafelków mapowych OpenStreetMap. Docelowy wygląd map powinien być własnym, uproszczonym stylem przewodnika, podporządkowanym czytelności i funkcji decyzyjnej.

Mapy mają pokazywać tylko potrzebne elementy, np. morze, ląd, główne drogi lub kierunki przejazdu, wybrane miejscowości, punkty z przewodnika, podpisy, ewentualne obszary oraz legendę. Nie mają udawać pełnej mapy nawigacyjnej.

Kolorystyka map SVG powinna być oparta na klasach i semantycznych zmiennych CSS, a nie na przypadkowych kolorach wpisanych bezpośrednio w każdym elemencie SVG. Należy zachować spójność z podejściem przyjętym w `assets/css/style.css` i opisanym w `techniczne/audyty/AUDYT-NAWIGACJI-I-HIERARCHII.md`, gdzie ogólne style strony są przygotowywane tokenami kolorów z myślą o przyszłym trybie ciemnym.

Przykładowe robocze tokeny map:

- `--map-water`;
- `--map-land`;
- `--map-road`;
- `--map-route`;
- `--map-point`;
- `--map-label`;
- `--map-muted-label`;
- `--map-border`.

Pierwszy wdrożony wariant mapy ma paletę jasną oraz paletę ciemną uruchamianą przez `@media (prefers-color-scheme: dark)`. Obie wersje korzystają z tej samej struktury SVG i różnią się wyłącznie semantycznymi zmiennymi CSS.

Przy projektowaniu kolorów należy osobno sprawdzić kontrast podpisów, punktów, linii tras, obszarów i tła. Elementy istotne informacyjnie nie powinny być rozróżniane wyłącznie kolorem; w razie potrzeby trzeba używać także kształtu, grubości linii, stylu linii, numerów punktów albo tekstowej legendy.

Pierwsza mapa potwierdziła kierunek techniczny: źródło pozostaje osobnym plikiem SVG w katalogu `_includes`, ale Jekyll osadza jego kod inline w wynikowym HTML. Pozwala to stylować mapę zmiennymi CSS strony i zachować jej nazwę oraz opis w drzewie dostępności dokumentu.

## Planowane poziomy map

Do dalszych testów przewidziane są przede wszystkim:

- mapa szerszego obszaru pokazująca położenie Dżerby oraz miejsc na południu Tunezji;
- osobna mapa orientacyjna Dżerby z najważniejszymi miejscami na wyspie;
- mapy konkretnych tras wycieczek, jeśli pomogą porównać programy;
- bardziej szczegółowa mapa pojedynczego miejsca tylko wtedy, gdy pojawi się realna potrzeba.

Nie łączymy szerokiej mapy południowej Tunezji i szczegółowej mapy Dżerby przez ramki, wstawki ani powiększenia wewnątrz jednej grafiki. Jeśli potrzebne są oba poziomy, przygotowujemy je jako osobne mapy umieszczone w odpowiednich miejscach sekcji `wycieczki.md`.

Pierwszym sensownym wzorcem do zaplanowania pozostaje układ map dla `wycieczki.md`: osobno mapa szerszego obszaru wycieczek i osobno mapa Dżerby, zanim powstaną kolejne warianty.

## Status

Na 24 sierpnia 2026 r. datowany snapshot OpenStreetMap dla Tunezji `tunisia-260822.osm.pbf` został pobrany, zweryfikowany sumami kontrolnymi i zapisany w archiwum danych źródłowych na Google Drive. Szczegóły znajdują się w `techniczne/mapy/snapshot-osm-tunezja.md`.

Pierwsza własna mapa SVG Dżerby została wygenerowana i umieszczona w Atlasie miejsc. Jest to wariant pilotażowy do oceny przed przygotowaniem mapy szerszego obszaru południowej Tunezji oraz ewentualnych dalszych map.
