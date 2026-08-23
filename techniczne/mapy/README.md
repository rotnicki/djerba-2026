# Mapy — dane źródłowe

Mapy przygotowywane dla przewodnika mają być oparte na rzeczywistych danych OpenStreetMap, a nie na grafikach generowanych przez AI.

Ten dokument dotyczy technicznej strony map. Ogólny plan materiałów wizualnych, w tym zdjęć reprezentujących miejsca w `wycieczki.md`, znajduje się w `techniczne/wizualizacje/README.md`.

## Dokumenty i narzędzia

- [pierwsza mapa Dżerby — specyfikacja, wdrożenie i odtwarzanie](mapa-dzerby.md);
- [manifest snapshotu OpenStreetMap dla Tunezji](snapshot-osm-tunezja.md);
- [generator mapy Dżerby](generate_djerba_map.py);
- [zależności generatora](requirements-djerba-map.txt).

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

Kod SVG znajduje się w `_includes/maps/djerba.svg` i jest osadzany inline przez Jekyll. Pełny zapis decyzji, parametrów danych, modelu dostępności, kolorów, procedury generowania i wyników kontroli znajduje się w dokumencie [Mapa Dżerby — specyfikacja, wdrożenie i odtwarzanie](mapa-dzerby.md).

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
