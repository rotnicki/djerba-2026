# Snapshot OSM Tunezji — manifest techniczny

Status: **snapshot pobrany, zweryfikowany i zapisany w archiwum Google Drive; plik PBF celowo nie jest przechowywany w publicznym repozytorium**.

Data przygotowania manifestu: 23 sierpnia 2026 r.

Ten plik opisuje źródłowy snapshot OpenStreetMap planowany do wykorzystania przy przygotowaniu map SVG dla przewodnika `Dżerba 2026`.

## Decyzja archiwizacyjna

Pełny plik `.osm.pbf` jest ciężkim, binarnym plikiem źródłowym. Nie zapisujemy go bezpośrednio w publicznym repozytorium GitHub.

W repozytorium zapisujemy:

- manifest techniczny;
- źródło pobrania;
- planowany zakres użycia;
- dane kontrolne pobranego pliku;
- lekkie pliki końcowe map, gdy zostaną przygotowane.

Pełny snapshot danych źródłowych jest zapisany w archiwum danych źródłowych:

`Google Drive: Dżerba 2026/Mapy – dane źródłowe`

https://drive.google.com/drive/folders/1WJh1QCaqH3ZNnX5Nks2TPib11TDDdwqN

## Źródło danych

Źródło: Geofabrik Download Server — Tunisia.

Strona informacyjna:

https://download.geofabrik.de/africa/tunisia.html

Stały adres najnowszego pliku źródłowego:

https://download.geofabrik.de/africa/tunisia-latest.osm.pbf

Pobrany plik datowany:

https://download.geofabrik.de/africa/tunisia-260822.osm.pbf

Format:

`.osm.pbf`

Charakter danych:

- wycinek danych OpenStreetMap dla całej Tunezji;
- bez nazw użytkowników, identyfikatorów użytkowników i identyfikatorów changesetów;
- przeznaczony do narzędzi takich jak Osmium, Osmosis, imposm, osm2pgsql, mkgmap i podobnych.

Geofabrik nie definiuje osobnych subregionów dla Tunezji. Do przygotowania mapy Dżerby i południowej Tunezji trzeba więc pobrać snapshot całego kraju, a następnie wyciąć lub przefiltrować potrzebny obszar lokalnie.

## Dane zapisanego snapshotu

- nazwa pliku: `tunisia-260822.osm.pbf`;
- data pobrania: 24 sierpnia 2026 r., około 00:35 CEST (23 sierpnia 2026 r., 22:35 UTC);
- data oznaczona w nazwie snapshotu Geofabrik: 22 sierpnia 2026 r.;
- rozmiar: `84 028 017` bajtów;
- SHA-256: `4629c6f40e1749f266fa339ba484f473414cbb026c7b6267a47f16715266bfaf`;
- MD5: `872548a5a57926f1451d1eb716ef7d46` — zgodna z sumą opublikowaną przez Geofabrik;
- format i typ MIME: `.osm.pbf`, `application/octet-stream`;
- lokalizacja: [Google Drive — tunisia-260822.osm.pbf](https://drive.google.com/file/d/1MZYSe-eAzNul0wcBEsQ9WWMpBdWtRNov/view?usp=drivesdk);
- narzędzie użyte do pobrania: `curl 8.5.0` z obsługą przekierowań, ponawiania i wznawiania;
- wykonawca techniczny: Codex, na polecenie Mikołaja Rotnickiego.

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

Pierwszym wykonanym zastosowaniem snapshotu była mapa Dżerby w dawnej, wspólnej stronie `wycieczki.md`. Obecnie obie mapy są publikowane w `atlas-miejsc.md`. Specyfikację, parametry i procedurę odtworzenia pierwszej mapy opisuje dokument [Mapa Dżerby — specyfikacja, wdrożenie i odtwarzanie](mapa-dzerby.md).

Dalsze wykorzystanie danych obejmuje:

1. wdrożoną mapę szerszego obszaru: Dżerba i południe Tunezji;
2. ewentualne późniejsze mapy tras, jeśli pomogą porównywać programy wycieczek.

Roboczy zasięg pierwszej mapy szerszego obszaru jest opisany w `techniczne/mapy/README.md`.

## Wynik operacji

24 sierpnia 2026 r. datowany snapshot został pobrany z Geofabrik, a jego lokalna suma MD5 została porównana z sumą opublikowaną przez dostawcę. Plik przesłano do folderu `Dżerba 2026/Mapy – dane źródłowe`. Odczyt kontrolny metadanych Google Drive potwierdził nazwę `tunisia-260822.osm.pbf`, typ `application/octet-stream` i rozmiar `84 028 017` bajtów.
