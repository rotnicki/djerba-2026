---
published: false
---

# Audyt i wdrożenie trybu ciemnego

Status: **tryb ciemny wdrożony i opublikowany 24 sierpnia 2026 r.; automatyczne kontrole kodu i publikacji zakończone pozytywnie, ręczny test na docelowych urządzeniach pozostaje do wykonania**.

Punkt wyjścia: `master` w commicie `5c3ebb9a77e981e70dba406d94c94acb5353dd53`.

Commit wdrażający kod i pierwszą wersję tego raportu: `7b40ce917de256e0f4d6e0060770fcdd5feb0446`.

Ten dokument opisuje rozszerzenie zatwierdzonego jasnego wyglądu strony o automatyczny tryb ciemny. Nie jest częścią publicznego przewodnika i pozostaje wyłączony z GitHub Pages razem z całym katalogiem `techniczne/`.

**Uzupełnienie po przebudowie materiałów o wycieczkach:** nowe tabele porównawcze korzystają wyłącznie z istniejących semantycznych tokenów kolorów. Ich nagłówki, podpisy, komórki i obramowania dziedziczą zatem wariant jasny, ciemny i wymuszonych kolorów bez osobnej palety.

## Założenia

- tryb jasny pozostaje zatwierdzoną wersją bazową;
- nie zmieniamy układu, typografii, hierarchii nagłówków ani charakteru wizualnego strony;
- tryb ciemny jest wybierany automatycznie przez `prefers-color-scheme`;
- nie dodajemy skryptu ani ręcznego przełącznika motywu;
- wykorzystujemy istniejące semantyczne zmienne CSS i komponenty;
- informacja nie może być przekazywana wyłącznie kolorem;
- mapa Dżerby zachowuje istniejące, wcześniej sprawdzone palety jasną, ciemną i wymuszonych kolorów.

## Zakres wykonanych zmian

Zmiany produkcyjne ograniczono do `assets/css/style.css`.

Wykonano:

1. dodanie `color-scheme: light` w wariancie bazowym i `color-scheme: dark` wewnątrz `@media (prefers-color-scheme: dark)`;
2. przypisanie ciemnych wartości istniejącym tokenom strony:
   - `--color-page-bg`;
   - `--color-surface`;
   - `--color-surface-strong`;
   - `--color-text`;
   - `--color-text-muted`;
   - `--color-border`;
   - `--color-border-strong`;
   - `--color-link`;
3. dodanie ciemnego tokenu `--color-focus`;
4. zastąpienie twardo wpisanego koloru skip linku tokenem `--color-skip-link-text`;
5. zachowanie w jasnym motywie dotychczasowej wartości skip linku `#111111`;
6. zastosowanie dla fokusu wartości `var(--color-focus, currentColor)`, dzięki czemu jasny wariant zachowuje wcześniejszy `currentColor`, a ciemny otrzymuje osobny, sprawdzony kolor;
7. zastosowanie analogicznego fallbacku dla fokusu przewijanego kontenera mapy: w trybie jasnym pozostaje dotychczasowy kolor linku;
8. rozszerzenie `@media (forced-colors: active)` o systemowe kolory głównych tokenów strony: `Canvas`, `CanvasText`, `LinkText` i `Highlight`.

Nie zastosowano globalnego `forced-color-adjust: none`. Przeglądarka i ustawienia użytkownika zachowują kontrolę nad kolorami wymuszonymi.

## Paleta ciemna strony

| Rola | Wartość |
| --- | --- |
| tło strony | `#0d1117` |
| zwykła powierzchnia | `#161b22` |
| mocniejsza powierzchnia | `#21262d` |
| tekst podstawowy | `#f0f6fc` |
| tekst pomocniczy | `#8b949e` |
| zwykłe obramowanie | `#30363d` |
| mocne obramowanie | `#6e7681` |
| link | `#58a6ff` |
| fokus | `#79c0ff` |

Paleta odpowiada kierunkowi zapisanemu wcześniej w `AUDYT-NAWIGACJI-I-HIERARCHII.md`.

## Zachowanie trybu jasnego

Jasne wartości istniejących tokenów nie zostały zmienione.

Zmiany, które dotyczą również kodu wariantu bazowego, zachowują wcześniejszy wynik:

- skip link nadal ma kolor `#111111`, lecz pobiera go z tokenu;
- fokus linków i przycisków nadal używa `currentColor`, ponieważ token ciemnego fokusu nie jest definiowany w wariancie jasnym;
- fokus kontenera mapy nadal używa jasnego `--color-link`;
- `color-scheme: light` jawnie opisuje dotychczasowy jasny wariant;
- nie zmieniono żadnej wartości dotyczącej rozmiaru, położenia, odstępu, szerokości, typografii ani reflow.

Nie zmieniono layoutu, nawigacji, publicznych dokumentów Markdown, kodu SVG ani generatora mapy.

## Kontrast

Automatycznie obliczone minimalne kontrasty dla elementów strony na trzech ciemnych powierzchniach — tle strony, zwykłej powierzchni i mocniejszej powierzchni:

| Element | Najniższy wynik |
| --- | ---: |
| tekst podstawowy | `13,98:1` |
| tekst pomocniczy | `4,95:1` |
| link | `6,03:1` |
| fokus | `7,82:1` |
| mocne obramowanie | `3,31:1` |

Istniejąca ciemna paleta mapy nie została zmieniona. Ponowna kontrola dała:

| Para na mapie | Wynik |
| --- | ---: |
| etykieta / ląd | `12,00:1` |
| etykieta / woda | `13,44:1` |
| droga / ląd | `6,15:1` |
| obrys / woda | `8,01:1` |
| tekst znacznika atrakcji / znacznik | `10,27:1` |
| tekst hotelu / znacznik hotelu | `10,69:1` |

Zwykłe obramowanie `--color-border` pozostaje delikatnym separatorem dekoracyjnym. Nie jest jedynym sygnałem stanu ani granicy elementu interaktywnego.

## Stany i informacja niezależna od koloru

- linki pozostają podkreślone, a `hover` zwiększa grubość podkreślenia;
- fokus ma obrys o grubości 3 px i odsunięciu 3 px;
- bieżąca pozycja nawigacji nadal ma pogrubienie i mocniejsze podkreślenie;
- hierarchię H2–H5 przekazują również rozmiar, grubość pisma, odstępy i obramowania;
- hotel na mapie ma romb i literę `H`, a atrakcje koła i numery;
- mapa ma nazwy miejsc i pełny tekstowy odpowiednik pod grafiką.

Publiczne strony nie zawierają obecnie tabel. Tabele w dokumentacji technicznej nie są publikowane przez GitHub Pages. Nie dodano więc nowego wizualnego komponentu tabeli, który zmieniałby zatwierdzony wygląd jasny. Ewentualna przyszła tabela publiczna odziedziczy tekst i tło aktualnego motywu, ale przed jej publikacją powinna otrzymać osobny test obramowań, reflow i nagłówków kolumn.

Obecny blok cytatu w `wycieczki.md`, kod inline i standardowe listy nie mają własnych twardo wpisanych kolorów i dziedziczą kolory aktualnego motywu.

## Wykonane kontrole automatyczne

- ponowne pobranie i porównanie lokalnego `master` z `origin/master` przed zmianą;
- potwierdzenie, że wszystkie wcześniejsze jasne tokeny zachowały identyczne wartości;
- kontrola obecności pełnego zestawu tokenów ciemnych;
- kontrola systemowych tokenów dla `forced-colors`;
- potwierdzenie braku `forced-color-adjust`;
- kontrola zbilansowania bloków CSS;
- `git diff --check`;
- ponowne obliczenie kontrastów strony i mapy;
- statyczne potwierdzenie zachowania pogrubienia i podkreślenia bieżącej nawigacji, obrysu fokusu oraz różnych kształtów oznaczeń mapy.

## Kontrola publikacji

Po zapisie do `master`:

- workflow `pages build and deployment`, run `32694403312` — `success`;
- workflow `Check links`, run `32694403991` — `success`;
- publiczna strona główna zawiera arkusz `/djerba-2026/assets/css/style.css`;
- publiczny arkusz zawiera `prefers-color-scheme`, ciemne tokeny strony i `forced-colors`;
- SHA-256 lokalnego i publicznego arkusza CSS jest identyczne: `a61d5c042a4cc5bd4fb0a44c59e8d98e469961969272ba850dc37cf12dfb6a2b`;
- próbny adres raportu w publicznej GitHub Pages zwraca `404`, co potwierdza dalsze wyłączenie katalogu `techniczne/` z publikacji.

## Kontrole ręczne po publikacji

Po publikacji należy jeszcze wykonać na docelowych urządzeniach:

1. porównanie jasnego wariantu z zatwierdzonym wyglądem;
2. ocenę strony głównej, długiej strony z nagłówkami H2–H5 i strony z mapą w trybie ciemnym;
3. przejście klawiaturą przez skip link, nawigację, linki, przyciski i przewijany kontener mapy;
4. test przy powiększeniu 200% i 400% oraz przy szerokości około 320 CSS px;
5. test VoiceOver z Safari na iPhonie i Macu;
6. pomocniczy test Windows High Contrast / `forced-colors` i NVDA.

## Werdykt

Zmiana jest minimalnym rozszerzeniem istniejącego systemu. Nie projektuje strony od początku, nie zmienia zatwierdzonego jasnego wyglądu i wykorzystuje wcześniejszą tokenizację oraz gotowy ciemny wariant mapy.

Automatyczna część kontroli oraz publikacja GitHub Pages zakończyły się pozytywnie. Pełne potwierdzenie jakości użytkowej wymaga jeszcze ręcznego testu wyrenderowanej GitHub Pages na docelowych urządzeniach.
