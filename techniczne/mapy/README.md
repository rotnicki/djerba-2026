# Mapy — dane źródłowe

Mapy przygotowywane dla przewodnika mają być oparte na rzeczywistych danych OpenStreetMap, a nie na grafikach generowanych przez AI.

Ten dokument dotyczy technicznej strony map. Ogólny plan materiałów wizualnych, w tym zdjęć reprezentujących miejsca w `wycieczki.md`, znajduje się w `techniczne/wizualizacje/README.md`.

## Cel map

Planowane mapy mają przede wszystkim pomagać w orientacji przestrzennej: pokazywać położenie ważnych miejsc, relacje między nimi oraz — tam, gdzie ma to sens — przebieg tras wycieczek.

Nie mają zastępować map nawigacyjnych ani tekstowego opisu. Mają być uproszczone i czytelne, również dla osób słabowidzących i widzących przewodników.

## Źródło danych

Planowane źródło: Geofabrik — wycinek danych OpenStreetMap dla Tunezji.

Pliki źródłowe mają być przechowywane jako zamrożony snapshot z konkretną datą, tak aby możliwe było późniejsze odtworzenie map z tych samych danych.

## Archiwum plików źródłowych

Google Drive: folder `Dżerba 2026/Mapy – dane źródłowe`

https://drive.google.com/drive/folders/1WJh1QCaqH3ZNnX5Nks2TPib11TDDdwqN

Po pobraniu snapshotu należy zapisać tutaj co najmniej:

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

## Planowane poziomy map

Do dalszych testów przewidziane są przede wszystkim:

- mapa orientacyjna Dżerby z najważniejszymi miejscami;
- mapa szerszego obszaru pokazująca położenie Dżerby oraz miejsc na południu Tunezji;
- mapy konkretnych tras wycieczek, jeśli pomogą porównać programy;
- bardziej szczegółowa mapa pojedynczego miejsca tylko wtedy, gdy pojawi się realna potrzeba.

Pierwszym sensownym wzorcem do wykonania pozostaje mapa `Dżerba — najważniejsze miejsca`, zanim powstaną kolejne warianty.

## Status

Na 23 sierpnia 2026 r. istnieje plan i miejsce archiwizacji danych źródłowych. Snapshot OpenStreetMap dla Tunezji nie został jeszcze pobrany i zamrożony, a własne mapy SVG nie zostały jeszcze przygotowane.
