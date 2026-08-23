# Snapshot OSM Tunezji — manifest techniczny

Status: **manifest przygotowany, plik źródłowy PBF nie jest zapisany w repozytorium**.

Data przygotowania manifestu: 23 sierpnia 2026 r.

Ten plik opisuje źródłowy snapshot OpenStreetMap planowany do wykorzystania przy przygotowaniu map SVG dla przewodnika `Dżerba 2026`.

## Decyzja archiwizacyjna

Pełny plik `.osm.pbf` jest ciężkim, binarnym plikiem źródłowym. Nie zapisujemy go bezpośrednio w publicznym repozytorium GitHub.

W repozytorium zapisujemy:

- manifest techniczny;
- źródło pobrania;
- planowany zakres użycia;
- wymagane dane kontrolne do uzupełnienia po rzeczywistym pobraniu pliku;
- lekkie pliki końcowe map, gdy zostaną przygotowane.

Pełny snapshot danych źródłowych powinien zostać zapisany w archiwum danych źródłowych:

`Google Drive: Dżerba 2026/Mapy – dane źródłowe`

https://drive.google.com/drive/folders/1WJh1QCaqH3ZNnX5Nks2TPib11TDDdwqN

## Źródło danych

Źródło: Geofabrik Download Server — Tunisia.

Strona informacyjna:

https://download.geofabrik.de/africa/tunisia.html

Planowany plik źródłowy:

https://download.geofabrik.de/africa/tunisia-latest.osm.pbf

Format:

`.osm.pbf`

Charakter danych:

- wycinek danych OpenStreetMap dla całej Tunezji;
- bez nazw użytkowników, identyfikatorów użytkowników i identyfikatorów changesetów;
- przeznaczony do narzędzi takich jak Osmium, Osmosis, imposm, osm2pgsql, mkgmap i podobnych.

Geofabrik nie definiuje osobnych subregionów dla Tunezji. Do przygotowania mapy Dżerby i południowej Tunezji trzeba więc pobrać snapshot całego kraju, a następnie wyciąć lub przefiltrować potrzebny obszar lokalnie.

## Informacje do uzupełnienia po pobraniu

Po rzeczywistym pobraniu i zapisaniu pliku w archiwum należy uzupełnić:

- dokładną nazwę zapisanego pliku;
- datę i godzinę pobrania;
- datę danych OSM wskazaną przez Geofabrik;
- rozmiar pliku w bajtach;
- sumę SHA-256;
- ewentualną sumę MD5, jeśli zostanie pobrana z Geofabrik;
- dokładną lokalizację pliku w archiwum;
- narzędzie użyte do pobrania;
- osobę wykonującą pobranie.

## Robocze polecenia kontrolne

Przykładowe pobranie:

```bash
curl -L -o tunisia-latest.osm.pbf https://download.geofabrik.de/africa/tunisia-latest.osm.pbf
```

Przykładowe obliczenie sumy SHA-256:

```bash
sha256sum tunisia-latest.osm.pbf
```

Przykładowe pobranie pomocniczego pliku `.poly` opisującego zakres Tunezji:

```bash
curl -L -o tunisia.poly https://download.geofabrik.de/africa/tunisia.poly
```

## Zakres użycia w projekcie

Pierwszym zastosowaniem snapshotu ma być przygotowanie map dla `wycieczki.md`:

1. mapa szerszego obszaru: Dżerba i południe Tunezji;
2. osobna mapa Dżerby;
3. ewentualnie późniejsze mapy tras, jeśli pomogą porównywać programy wycieczek.

Roboczy zasięg pierwszej mapy szerszego obszaru jest opisany w `techniczne/mapy/README.md`.

## Uwaga o tej sesji

W tej sesji przygotowano manifest i zapisano odniesienia w repozytorium. Nie potwierdzono zapisu pełnego pliku `.osm.pbf` w archiwum danych źródłowych i nie obliczono jego sumy SHA-256.
