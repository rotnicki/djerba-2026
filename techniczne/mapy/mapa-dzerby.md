# Mapa Dżerby — specyfikacja, wdrożenie i odtwarzanie

Status: **pierwsza wersja pilotażowa wdrożona 24 sierpnia 2026 r. w `wycieczki.md` i opublikowana w GitHub Pages**.

Korekta po pierwszej ocenie użytkownika: dodano brakującą podziałkę 0–10 km, rozsunięto oznaczenia 2 i 3, przeniesiono linie prowadzące pod warstwę znaczników oraz poprawiono legendę HTML na listę numerowaną.

Ten dokument jest technicznym zapisem ustaleń podjętych przed wygenerowaniem pierwszej mapy Dżerby, jej aktualnej implementacji oraz procedury ponownego utworzenia i sprawdzenia. Nie jest treścią dla uczestników wyjazdu.

Dokumenty i pliki powiązane:

- [ogólne zasady map w projekcie](README.md);
- [manifest snapshotu OpenStreetMap dla Tunezji](snapshot-osm-tunezja.md);
- [generator SVG](generate_djerba_map.py);
- [zależności generatora](requirements-djerba-map.txt);
- wynikowy plik `_includes/maps/djerba.svg`;
- miejsce publikacji i tekstowy opis mapy w `wycieczki.md`;
- style mapy w `assets/css/style.css`.

Pierwsze wdrożenie kodu mapy: [commit `f4973f0`](https://github.com/rotnicki/djerba-2026/commit/f4973f0d5b580b08358a7eaecc96dee4a84367f1). Wynik można ocenić na publicznej stronie [Wycieczki i miejsca — sekcja Dżerba](https://rotnicki.github.io/djerba-2026/wycieczki.html#d%C5%BCerba).

## Cel i granice pierwszej wersji

Mapa ma pomóc uczestnikom zrozumieć, gdzie względem hotelu znajdują się potencjalne atrakcje opisane w przewodniku. Jest narzędziem orientacyjnym i decyzyjnym przy wyborze wycieczek.

Mapa nie jest:

- mapą nawigacyjną;
- planem wszystkich ulic i budynków;
- pełnym katalogiem punktów OpenStreetMap;
- odwzorowaniem dokładnych tras przejazdu organizatorów;
- interaktywną aplikacją mapową.

Pierwsza wersja celowo pokazuje jedynie:

- morze i zarys wyspy;
- wybrane drogi główne;
- hotel Club Palm Azur jako stały punkt odniesienia;
- miejsca z części Atlasu dotyczącej Dżerby;
- dwa pomocnicze punkty orientacyjne: Midoun i El Kantarę;
- nazwy miejsc, strzałkę północy i liniową podziałkę od 0 do 10 km.

Nie dodano wszystkich dróg lokalnych, budynków, granic administracyjnych, przypadkowych punktów usługowych ani dekoracyjnych szczegółów terenu. Takie dane zwiększałyby zagęszczenie bez poprawy realizacji celu mapy.

## Dwa osobne poziomy map

Ustalono, że szczegółowej mapy Dżerby nie należy łączyć z mapą południowej Tunezji przez ramkę, wstawkę ani powiększenie wewnątrz jednej grafiki.

Plan obejmuje dwa osobne materiały:

1. wdrożoną mapę Dżerby z hotelem i miejscami na wyspie;
2. planowaną mapę szerszego obszaru, pokazującą skalę wyjazdów z Dżerby na południe Tunezji.

Mapa Dżerby jest umieszczona w `wycieczki.md` w sekcji `## Atlas miejsc`, bezpośrednio po nagłówku `### Dżerba` i przed pierwszym nagłówkiem H4 tej części.

Planowana mapa południowej Tunezji ma zostać umieszczona osobno, roboczo po nagłówku `### Wyjazd z Dżerby na kontynent`. Jej ostateczne położenie należy jeszcze ocenić razem z pierwszym renderem tej mapy.

## Zakres geograficzny i parametry renderowania

Ramka danych pierwszej mapy:

- zachód: `10.73°E`;
- wschód: `11.09°E`;
- południe: `33.65°N`;
- północ: `33.95°N`.

Parametry SVG:

- `viewBox`: `0 0 960 760`;
- margines poziomy: `54` jednostki SVG;
- margines pionowy: `58` jednostek SVG;
- projekcja robocza: lokalne odwzorowanie equirektangularne ze skalowaniem długości geograficznej przez cosinus średniej szerokości geograficznej obszaru;
- uproszczenie linii brzegowej: `0.00035°` z zachowaniem topologii;
- uproszczenie dróg: `0.00025°` z zachowaniem topologii;
- pominięcie fragmentów dróg krótszych niż `0.0025°` w geometrii roboczej.
- podziałka: odcinek `10 km` obliczany z tej samej skali lokalnej projekcji i umieszczany w prawym dolnym rogu; znacznik pośredni odpowiada `5 km`.

Wartości uproszczeń są parametrami renderowania mapy wyspy. Nie są dokładnością pomiarową i nie należy używać SVG do wyznaczania tras ani odległości.

Generator wybiera drogi OSM klas `primary` i `secondary`, przycina je do obszaru wyspy i usuwa krótkie fragmenty, które w tej skali odpowiadają głównie rondom, łącznikom i podwójnym odcinkom jezdni.

## Punkty pokazane na mapie

Numery obiektów OpenStreetMap są celowo zapisane w generatorze, aby mapa była odtwarzalna z zamrożonego snapshotu.

| Oznaczenie | Miejsce | Obiekt OSM | Rola na mapie |
| --- | --- | --- | --- |
| H | hotel Club Palm Azur | węzeł `1123865146` | główny punkt odniesienia, romb |
| 1 | Houmt Souk i fort Borj Ghazi Mustapha | węzeł `9335010754` | atrakcja, położenie przy forcie |
| 2 | Erriadh i Djerbahood | węzeł `297765267` | atrakcja |
| 3 | synagoga El Ghriba | węzeł `297765095` | atrakcja |
| 4 | Guellala | węzeł `1259516109` | atrakcja |
| 5 | Djerba Explore | obiekt typu `way` `213910588` | atrakcja, punkt wyprowadzony z geometrii obiektu |
| 6 | Ras Rmel | węzeł `10820734092` | atrakcja |
| bez numeru | Midoun | węzeł `287613682` | pomocniczy punkt orientacyjny |
| bez numeru | El Kantara | węzeł `6616525005` | kierunek grobli i wyjazdu na kontynent |

Położenia pochodzą z `tunisia-260822.osm.pbf`. Ręcznie ustawiane są jedynie przesunięcia etykiet i prowadzących do nich linii, aby ograniczyć kolizje tekstu. Ponieważ punkty 2 i 3 dzieli mniej niż kilometr, ich numerowane koła są kartograficznie rozsunięte. Małe punkty zachowują dokładne położenia, a krótkie linie łączą je z przesuniętymi oznaczeniami.

Linie prowadzące są zapisywane w SVG przed warstwą znaczników. Dzięki temu koła, romb i cyfry są zawsze rysowane na liniach, a nie pod nimi. Generator dodatkowo przerywa pracę, jeżeli odległość między środkami dwóch numerowanych oznaczeń jest mniejsza niż suma ich promieni i czterech jednostek odstępu.

## Źródło i pochodzenie danych

Źródłem jest datowany wycinek Geofabrik oparty na OpenStreetMap:

- plik: `tunisia-260822.osm.pbf`;
- rozmiar: `84 028 017` bajtów;
- SHA-256: `4629c6f40e1749f266fa339ba484f473414cbb026c7b6267a47f16715266bfaf`;
- MD5: `872548a5a57926f1451d1eb716ef7d46`;
- archiwum: [Google Drive — tunisia-260822.osm.pbf](https://drive.google.com/file/d/1MZYSe-eAzNul0wcBEsQ9WWMpBdWtRNov/view?usp=drivesdk).

Pełny PBF pozostaje poza publicznym repozytorium. W repozytorium są przechowywane manifest, generator i lekki wynik SVG.

Przy mapie publicznej musi pozostać widoczna atrybucja `© OpenStreetMap contributors, ODbL` z odnośnikiem do zasad OpenStreetMap.

## Architektura wdrożenia

Plik `_includes/maps/djerba.svg` zawiera samo SVG bez stylów wpisanych na stałe w elementy. W `wycieczki.md` jest wstawiany przez Jekyll:

```liquid
{% include maps/djerba.svg %}
```

Wynikowa strona zawiera kod SVG bezpośrednio w HTML. Nie korzysta z elementu `img`, `object`, `iframe` ani zewnętrznego pliku ładowanego przez przeglądarkę.

Rozdzielono dwie odpowiedzialności:

- `_includes/maps/djerba.svg` — geometria, klasy semantyczne, widoczne etykiety, tytuł i krótki opis;
- `assets/css/style.css` — kolory, grubości linii, typografia, zachowanie responsywne, tryb ciemny i wymuszone kolory.

Takie rozwiązanie zachowuje jeden odtwarzalny plik źródłowy mapy, a jednocześnie pozwala stylować go zgodnie z motywem strony i udostępniać semantykę SVG w drzewie dostępności dokumentu.

Mapa jest obecnie wstawiana tylko raz na stronie. Identyfikatory `djerba-map-title` i `djerba-map-desc` są globalne w dokumencie. Przed ponownym użyciem tej samej mapy na jednej stronie trzeba najpierw zapewnić unikatowe identyfikatory.

## Dostępność

### Przyjęty model

Pierwsza wersja jest statyczną, atomową grafiką:

- główny element SVG ma `role="img"`;
- `aria-labelledby` wskazuje elementy `title` i `desc`;
- `title` identyfikuje mapę;
- `desc` objaśnia znaczenie litery H i numerów 1–6, informuje o podziałce 0–10 km oraz wskazuje, że dokładniejszy opis znajduje się pod mapą;
- wewnętrzne warstwy dróg, etykiet i punktów mają `aria-hidden="true"`.

Nie wystawiono każdej drogi, linii brzegowej i etykiety jako osobnego przystanku czytnika ekranu. Surowa kolejność setek elementów SVG nie przekazywałaby relacji przestrzennych i znacznie wydłużałaby nawigację.

### Tekstowy odpowiednik

Bezpośrednio po mapie w zwykłym HTML znajduje się nagłówek `Opis mapy i relacje przestrzenne`, a pod nim:

- lista przypisująca literę i numery do nazw miejsc;
- położenie hotelu przy południowo-wschodnim wybrzeżu;
- kierunki względem hotelu;
- przybliżone odległości w linii prostej;
- informacja, że Erriadh/Djerbahood i El Ghriba tworzą bliską parę miejsc;
- informacja, że El Kantara wskazuje kierunek grobli i wyjazdu na kontynent;
- zastrzeżenie, że trasy drogowe są dłuższe.

Nie ograniczono odpowiednika mapy do tabeli nazw. Opis zachowuje najważniejsze informacje przestrzenne potrzebne do porównania miejsc.

Odległości w tekście obliczono geodezyjnie dla elipsoidy WGS84 i zaokrąglono odpowiednio do orientacyjnej funkcji materiału. Nie są one pobierane z tras samochodowych.

### Rozróżnianie wizualne

Informacja nie zależy wyłącznie od koloru:

- hotel ma romb oraz literę H;
- atrakcje mają koła oraz numery;
- każdy punkt ma widoczną nazwę;
- dodatkowa lista pod mapą ponownie łączy oznaczenia z nazwami.

Na wąskim ekranie SVG zachowuje minimalną szerokość `48rem`, a jego kontener może być przewijany poziomo. Kontener ma nazwę regionu i może otrzymać fokus klawiatury. Tekstowy odpowiednik pozostaje zwykłą, przelewającą się treścią HTML.

### Podstawa przyjętych decyzji

- [W3C WAI — Complex Images](https://www.w3.org/WAI/tutorials/images/complex/) wymienia mapy jako obrazy złożone i zaleca krótką identyfikację oraz dłuższy odpowiednik istotnych informacji.
- [W3C WAI — WCAG 2.2, kryterium 1.1.1 Non-text Content](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html) wymaga tekstowego odpowiednika realizującego równoważny cel.
- [W3C — SVG Accessibility API Mappings](https://www.w3.org/TR/svg-aam-1.0/) opisuje mapowanie semantyki SVG do interfejsów dostępności.
- [W3C — WAI-ARIA Graphics Module](https://www.w3.org/TR/graphics-aria-1.0/) opisuje role dla bardziej złożonych i strukturalnych grafik. W statycznej pierwszej wersji nie przyjęto drobnoziarnistej nawigacji po grafice, ponieważ jej cel skuteczniej realizuje jedna nazwana grafika i uporządkowany opis HTML.
- [Map Equivalent-Purpose Framework](https://arxiv.org/abs/2512.05310) jest źródłem badawczym, nie normą. Wzmacnia decyzję, aby tekstowy odpowiednik obejmował nie tylko nazwy, lecz także ogólne informacje przestrzenne i relacje między miejscami.

Przed wdrożeniem porównano także dwa wcześniejsze repozytoria użytkownika:

- [`rotnicki/racing-circuit-names`](https://github.com/rotnicki/racing-circuit-names) — potwierdziło użyteczność atomowego SVG z `role="img"`, `aria-labelledby`, `title` i `desc` jako prostego punktu wyjścia;
- [`rotnicki/a11y-svg-map`](https://github.com/rotnicki/a11y-svg-map) — zawiera eksperymenty z bardziej szczegółową semantyką poszczególnych obiektów mapy. Wzorców nie kopiowano mechanicznie; pierwsza mapa Dżerby celowo pozostaje jedną grafiką z pełniejszym opisem HTML.

Docelowe testy czytników ekranu należy prowadzić przede wszystkim w VoiceOver z Safari na iPhonie i Macu, a pomocniczo także w NVDA. Wyników ręcznego testu nie należy uznawać za potwierdzone, dopóki nie zostaną wykonane i zapisane.

## Kolory i kontrast

OpenStreetMap jest źródłem danych, nie wzorem kolorystycznym. Mapa ma własny uproszczony styl przewodnika.

| Rola | Tryb jasny | Tryb ciemny |
| --- | --- | --- |
| woda | `#dceff5` | `#102f3a` |
| ląd | `#f6edcf` | `#30352a` |
| drogi | `#756b59` | `#c7b47d` |
| atrakcje | `#7a1f3d` | `#f3b63f` |
| tekst atrakcji | `#ffffff` | `#17120a` |
| hotel | `#005d6a` | `#65d4e2` |
| tekst hotelu | `#ffffff` | `#071517` |
| główne etykiety | `#17252a` | `#f7fafb` |
| etykiety pomocnicze | `#3e565e` | `#d2e0e4` |
| obrys wyspy | `#315c68` | `#9bcbd8` |

Tryb ciemny jest wybierany przez `@media (prefers-color-scheme: dark)`. Dla `@media (forced-colors: active)` używane są kolory systemowe, m.in. `Canvas`, `CanvasText`, `Highlight` i `HighlightText`.

Zmierzony kontrast głównych par kolorów:

| Para | Jasny | Ciemny |
| --- | ---: | ---: |
| etykieta / ląd | 13,44:1 | 12,00:1 |
| etykieta / woda | 13,27:1 | 13,44:1 |
| droga / ląd | 4,48:1 | 6,15:1 |
| obrys / woda | 6,19:1 | 8,01:1 |
| tekst znacznika atrakcji / znacznik | 10,04:1 | 10,27:1 |
| tekst hotelu / znacznik hotelu | 7,57:1 | 10,69:1 |

Wartości dotyczą zdefiniowanych głównych teł. Przy każdej zmianie palety należy ponownie sprawdzić tekst według WCAG 2.2, kryterium 1.4.3 oraz informacyjne elementy nietekstowe według kryterium 1.4.11.

## Odtworzenie mapy

Poniższe polecenia należy wykonywać z katalogu głównego repozytorium.

### 1. Przygotowanie środowiska

Testowane środowisko: Python 3.12.

```bash
python -m venv /tmp/djerba-map-venv
source /tmp/djerba-map-venv/bin/activate
python -m pip install --disable-pip-version-check \
  -r techniczne/mapy/requirements-djerba-map.txt
```

### 2. Pozyskanie i sprawdzenie snapshotu

Plik można pobrać z archiwum Google Drive wskazanego w manifeście albo z datowanego adresu Geofabrik:

```bash
curl -L --fail --retry 3 --retry-delay 2 --continue-at - \
  --output /tmp/tunisia-260822.osm.pbf \
  https://download.geofabrik.de/africa/tunisia-260822.osm.pbf

sha256sum /tmp/tunisia-260822.osm.pbf
md5sum /tmp/tunisia-260822.osm.pbf
```

Przed generowaniem obie sumy muszą odpowiadać wartościom w manifeście. Nie należy zastępować pliku wersją `latest`, jeżeli celem jest dokładne odtworzenie tej mapy.

### 3. Generowanie SVG

```bash
python techniczne/mapy/generate_djerba_map.py \
  /tmp/tunisia-260822.osm.pbf \
  _includes/maps/djerba.svg
```

Generator:

1. odczytuje zamrożony PBF;
2. zbiera linie `natural=coastline`;
3. rekonstruuje wielokąt Dżerby;
4. wybiera i upraszcza drogi `primary` i `secondary`;
5. odczytuje skonfigurowane obiekty OSM;
6. przelicza współrzędne na układ SVG;
7. rozsuwa skonfigurowane bliskie oznaczenia i sprawdza brak kolizji numerowanych kół;
8. dodaje podziałkę 0–10 km, znaczniki, etykiety, tytuł, opis i metadane snapshotu;
9. zapisuje plik wynikowy.

W środowisku użytym 24 sierpnia 2026 r. dwukrotne uruchomienie po korekcie dało identyczny wynik. Aktualny SHA-256 wygenerowanego `_includes/maps/djerba.svg` wynosi:

`204fd8ea196069e2cb6d00108abad9f8a0e436b0d392f869b280111599d19d51`

Historyczna suma pierwszej wersji przed dodaniem podziałki i korektą kolizji wynosiła:

`d2b02aa338c4bfeea1e7f726d06bec7f469b6780bb2e5c0e583ddebf7b1711bb`

Zmiana generatora, zależności, danych lub etykiet może prawidłowo zmienić tę sumę. W takim przypadku należy zapisać nowy wynik kontroli w historii zmian lub zaktualizować ten dokument.

## Kontrola po wygenerowaniu

Minimalna checklista:

1. sprawdzić sumy snapshotu;
2. uruchomić generator dwukrotnie i porównać sumy SVG;
3. sprawdzić poprawność XML;
4. potwierdzić dokładnie jeden `title`, jeden `desc` i unikatowe identyfikatory;
5. potwierdzić `role="img"` oraz prawidłowe `aria-labelledby`;
6. wyrenderować i obejrzeć wariant jasny oraz ciemny;
7. sprawdzić podziałkę, kolizje etykiet, czytelność numerów, kolejność warstw linii i granice widoku;
8. ponownie obliczyć kontrast po każdej zmianie kolorów;
9. zbudować stronę Jekyll i potwierdzić, że SVG znajduje się inline w wynikowym HTML;
10. sprawdzić widok wąski i obsługę poziomego przewijania klawiaturą;
11. sprawdzić tekstowy opis oraz jego zgodność z punktami mapy;
12. wykonać ręczny test VoiceOver i zapisać jego wynik;
13. potwierdzić obecność atrybucji OpenStreetMap;
14. uruchomić kontrolę linków i publikację GitHub Pages.

Kontrole wykonane dla pierwszego wdrożenia:

- zgodność SHA-256 i MD5 snapshotu — potwierdzona;
- deterministyczne generowanie SVG — potwierdzone;
- poprawność XML, unikatowe identyfikatory, `title`, `desc`, rola i nazwa — potwierdzone;
- render jasny i ciemny — sprawdzony wizualnie;
- kontrast głównych par — obliczony i zapisany wyżej;
- struktura wynikowego HTML i osadzenie inline — potwierdzone;
- publikacja GitHub Pages — zakończona powodzeniem;
- automatyczna kontrola nowych odnośników dokumentacji — bez błędów; kontrola całego repozytorium zatrzymała się na przekroczeniach czasu zewnętrznych serwisów;
- ręczny test VoiceOver na urządzeniu użytkownika — **jeszcze niewykonany**;
- pomocniczy test NVDA — **jeszcze niewykonany**.

## Zasady utrzymania

Przy zmianie miejsc lub oznaczeń trzeba równocześnie:

1. zmienić konfigurację `POIS` lub `CONTEXT_NODES` w generatorze;
2. ponownie wygenerować SVG;
3. zaktualizować `desc` mapy;
4. zaktualizować listę i opis przestrzenny w `wycieczki.md`;
5. sprawdzić etykiety, kontrast, oba motywy i wymuszone kolory;
6. powtórzyć kontrolę dostępności i publikacji.

Jeżeli w przyszłości punkty staną się interaktywne, trzeba ponownie zaprojektować:

- kolejność fokusu;
- nazwy i cele elementów interaktywnych;
- obsługę klawiatury i dotyku;
- relację między mapą a sekcjami Atlasu;
- model semantyczny SVG;
- zachowanie w VoiceOver i innych czytnikach ekranu.

Nie należy automatycznie udostępniać czytnikowi ekranu wszystkich surowych ścieżek SVG.

Aktualizację snapshotu OSM należy traktować jako osobną, świadomą zmianę danych. Nowy snapshot wymaga nowego manifestu lub aktualizacji manifestu, zapisania sum kontrolnych, ponownej weryfikacji punktów i pełnego wygenerowania mapy.

## Otwarte działania

- ręczna ocena pierwszej wersji przez użytkownika, w tym VoiceOver na iPhonie i Macu;
- ewentualna korekta etykiet, poziomu szczegółowości lub opisu przestrzennego po ocenie;
- przygotowanie osobnej mapy południowej Tunezji;
- rozważenie map konkretnych tras dopiero wtedy, gdy przyniosą wyraźną korzyść przy porównywaniu programów.
