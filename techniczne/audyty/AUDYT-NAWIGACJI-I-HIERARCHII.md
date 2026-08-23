# Audyt nawigacji, hierarchii nagłówków i struktury wizualnej

Status: raport techniczny, nieprzeznaczony do publikacji jako strona przewodnika.

Zakres: niezależny audyt bieżącej struktury publicznych stron przewodnika Dżerba 2026 pod kątem nawigacji wewnętrznej, hierarchii nagłówków, czytelności wizualnej, dostępności klawiaturowej, powiększenia i obsługi czytnikami ekranu.

Raport nie otwiera ponownie zakończonego audytu merytorycznego etapu 12 i nie zmienia jego ustaleń.

## Stan bieżący

Publiczna nawigacja obejmuje stronę startową oraz dziewięć stron tematycznych:

- Praktyczne informacje
- Zdrowie
- Co zabrać
- Co kupić przed wyjazdem
- Łączność
- Pieniądze i płatności
- Wycieczki i miejsca
- Kultura i zwyczaje
- Język i zwroty

Obecny szablon posiada:

- odnośnik „Przejdź do treści”;
- semantyczny element `nav` z etykietą „Główna nawigacja”;
- `aria-current="page"` dla bieżącej strony;
- pojedynczy główny obszar `main`;
- elastyczną szerokość treści;
- widoczny styl fokusu;
- responsywną zmianę układu nawigacji na małych ekranach.

Nie stwierdzono systemowego pomijania poziomów nagłówków. Każda publiczna strona ma jeden nagłówek H1 dokumentu.

## Główne wnioski

Największa potrzeba nie dotyczy naprawy semantyki nagłówków, lecz:

1. ułatwienia szybkiego przechodzenia do głównych części dłuższych stron;
2. mocniejszego wizualnego rozróżnienia poziomów H2–H5;
3. zachowania prostoty przy dużym powiększeniu i na wąskich ekranach;
4. przygotowania stylów tak, aby późniejsze wprowadzenie trybu ciemnego nie wymagało przebudowy struktury.

## Numerowanie nagłówków

Nie rekomenduje się wprowadzania numeracji typu `1`, `1.1`, `1.1.1`.

Powody:

- zwiększa ilość tekstu odczytywanego przez czytniki ekranu;
- tworzy dodatkowy szum wizualny;
- łatwo traci aktualność przy zmianach kolejności sekcji;
- nie daje istotnej korzyści, jeżeli istnieją prawidłowe nagłówki, spis treści i wyraźna hierarchia wizualna.

## Główny spis treści „Na tej stronie”

Rekomendacja: zastosować lokalny spis treści na wszystkich dziewięciu stronach tematycznych.

Nie stosować go na `index.md`, ponieważ strona startowa sama pełni funkcję strony nawigacyjnej i ma prostą strukturę.

### Zakres spisu

Główny spis powinien obejmować wyłącznie nagłówki H2.

Nie należy umieszczać w nim H3, H4 ani H5. Dzięki temu lista pozostanie krótka i użyteczna także w VoiceOver oraz przy dużym powiększeniu.

### Położenie

Spis powinien znajdować się:

1. po H1;
2. po metadanych lub krótkim wprowadzeniu, jeśli występują;
3. przed pierwszym H2.

### Forma

Rekomendowana forma:

- zwykły element `nav` w przepływie dokumentu;
- widoczna etykieta „Na tej stronie”;
- lista nieuporządkowana;
- bez układu wielokolumnowego;
- bez przyklejonego panelu bocznego;
- domyślnie rozwinięty, nieukrywany w `details`;
- etykieta „Na tej stronie” nie powinna być nagłówkiem H2, aby nie zanieczyszczać hierarchii dokumentu i samego spisu treści.

Najlepiej zastosować współdzielony komponent, np. `_includes/page-toc.html`, zamiast duplikowania pełnego znacznika na każdej stronie.

Kramdown może automatycznie generować dokumentowy spis treści i identyfikatory nagłówków. Do głównego spisu H2 jest to wystarczające i należy unikać ręcznego utrzymywania osobnych list odnośników.

## Lokalne spisy sekcji

Nie należy dodawać ich wszędzie. Powinny być używane wyłącznie w bardzo rozbudowanych sekcjach.

Najlepsi kandydaci:

### `praktyczne.md`

Lokalny spis H3 w sekcji:

- „Odyseusz MSZ – warto zgłosić podróż”.

### `lacznosc.md`

Lokalny spis H3 w sekcji:

- „Internet poza hotelem — podróżne eSIM i pakiety danych”.

Można później przetestować wyjątkowy lokalny indeks operatorów H4, ponieważ użytkownik może szukać konkretnej marki. Nie należy jednak dodawać H4 do głównego spisu strony.

### `zdrowie.md`

Lokalne spisy H3 są szczególnie użyteczne w sekcjach:

- „Słońce, promieniowanie UV i upał”;
- „Bezpieczeństwo w morzu i na plaży przy hotelu Club Palm Azur”;
- sekcji dotyczącej biegunki podróżnych.

### `wycieczki.md`

Lokalne spisy H3 są szczególnie użyteczne w sekcjach:

- „Atlas miejsc”;
- „Programy wycieczek – porównujemy zawartość, nie tylko nazwę”;
- „Organizatorzy i wybór oferty”.

### Ograniczenie techniczne

Natywny automatyczny TOC Kramdown działa dla całego dokumentu. `toc_levels` filtruje poziomy nagłówków, ale nie ogranicza automatycznie spisu do pojedynczej sekcji H2.

Dlatego lokalnych spisów sekcji nie należy teraz utrzymywać ręcznie. Powinny być osobnym etapem technicznym po wdrożeniu i przetestowaniu głównego spisu H2.

## Hierarchia wizualna nagłówków

Rekomendowany język wizualny:

### H2

Najsilniejszy separator sekcji:

- wyraźniejsze neutralne tło;
- mocniejsza linia lub obramowanie;
- wewnętrzny padding;
- wyraźnie większy odstęp nad nagłówkiem niż pod nim.

### H3

Poziom słabszy niż H2:

- bez pełnego kolorowego tła;
- mocna pionowa linia po lewej stronie nagłówka;
- niewielki padding po lewej;
- jednoznacznie widoczny rozmiar i grubość pisma.

### H4

Przede wszystkim typografia i odstępy:

- bez pełnego tła;
- wyraźna grubość pisma;
- rozmiar nieznacznie większy od tekstu podstawowego;
- ewentualnie delikatny separator tylko wtedy, jeśli testy pokażą taką potrzebę.

### H5

H5 występuje obecnie w `wycieczki.md`, dlatego musi mieć jawnie zdefiniowany styl. Nie powinien pozostawać zależny od domyślnych stylów przeglądarki ani wyglądać jak drobny tekst pomocniczy.

Nie potrzebuje osobnego tła ani ramki.

## Wcięcia treści

Nie należy przesuwać całej zawartości sekcji H3/H4 w prawo.

Akapity i listy powinny zachowywać wspólną stabilną lewą krawędź. Hierarchię należy pokazywać na samych nagłówkach, a nie przez zmniejszanie dostępnej szerokości treści.

Jest to szczególnie ważne przy powiększeniu 200–400% i szerokościach odpowiadających urządzeniom mobilnym.

## Odstępy

Wartości do pilotażu, nie jako ostateczny standard:

- H2: margines górny około `3–3.5rem`, dolny około `1rem`;
- H3: górny około `2.5rem`, dolny około `0.7rem`;
- H4: górny około `1.75–2rem`, dolny około `0.5rem`.

Dodatkowo warto zastosować `scroll-margin-top` dla nagłówków będących celami odnośników.

Nie rekomenduje się wymuszania `scroll-behavior: smooth`.

## Kolory i tokeny semantyczne

Przed zmianą wyglądu zaleca się przejście z pojedynczych wartości kolorów na semantyczne zmienne CSS.

Proponowany zestaw pilotażowy:

| Zmienna | Tryb jasny | Przyszły tryb ciemny |
| --- | --- | --- |
| `--color-page-bg` | `#ffffff` | `#0d1117` |
| `--color-surface` | `#f6f8fa` | `#161b22` |
| `--color-surface-strong` | `#eaeef2` | `#21262d` |
| `--color-text` | `#1f2328` | `#f0f6fc` |
| `--color-text-muted` | `#57606a` | `#8b949e` |
| `--color-border` | `#d0d7de` | `#30363d` |
| `--color-border-strong` | `#656d76` | `#6e7681` |
| `--color-link` | `#0757a3` | `#58a6ff` |
| `--color-focus` | `#005fcc` | `#79c0ff` |

Najpierw należy wdrożyć wyłącznie wariant jasny. Tryb ciemny powinien być osobnym, później zatwierdzonym etapem.

## Spójność powierzchni

Rekomendowana rola elementów:

- tło strony — płótno;
- nagłówek i stopka — delikatna powierzchnia;
- lokalny spis treści — delikatna powierzchnia i zwykła ramka;
- H2 — mocniejsza powierzchnia;
- H3 — tło przezroczyste i mocna pionowa linia;
- H4 — rozwiązanie typograficzne;
- fokus — osobny kolor akcentowy.

Nie należy nadawać każdemu poziomowi nagłówka osobnego przypadkowego koloru. Hierarchia musi pozostać czytelna także w skali szarości.

## Kontrast i fokus

Bieżące podstawowe kolory tekstu i odnośników mają mocny kontrast względem aktualnego jasnego tła.

Obecne jasne obramowanie `#d0d7de` jest odpowiednie jako separator dekoracyjny, ale nie powinno być jedynym sygnałem istotnego stanu lub granicy interaktywnego komponentu.

Obecny styl `:focus-visible` jest dobrą podstawą. Przy tokenizacji należy zachować równie jednoznaczny fokus i przypisać go do zmiennej `--color-focus`.

## Reflow i powiększenie

Rozwiązania powinny zostać sprawdzone przynajmniej przy:

- 100%;
- 200%;
- 400%;
- wąskim widoku około 320 CSS px;
- układzie mobilnym.

Z tego powodu preferowany jest spis treści w normalnym przepływie dokumentu, a nie stały panel boczny.

## Czytniki ekranu

Główne zasady:

- semantyczna hierarchia nagłówków powinna odpowiadać hierarchii wizualnej;
- główny spis treści powinien być osobnym obszarem `nav` z jednoznaczną nazwą;
- H2-only ogranicza długość listy odczytywanej przez czytnik;
- nawigacja po nagłówkach nadal pozostaje pełnoprawną alternatywą dla spisu;
- nie należy automatycznie doklejać do wszystkich nagłówków ikon/permalinków, ponieważ zwiększałyby liczbę dodatkowych elementów odczytywanych przez czytniki.

## Ocena poszczególnych stron

| Plik | Najgłębszy poziom | Główny spis H2 | Lokalny spis |
| --- | --- | --- | --- |
| `index.md` | H2 | nie | nie |
| `praktyczne.md` | H4 | tak | H3 w sekcji Odyseusz |
| `zdrowie.md` | H4 | tak | wybrane rozbudowane H2 |
| `co-zabrac.md` | H3 | tak | nie |
| `co-kupic-przed-wyjazdem.md` | H2 | tak | nie |
| `lacznosc.md` | H4 | tak | H3 w sekcji eSIM; ewentualnie późniejszy test indeksu H4 operatorów |
| `pieniadze.md` | H4 | tak | nie |
| `wycieczki.md` | H5 | tak | kilka lokalnych H3 |
| `kultura-i-zwyczaje.md` | H3 | tak | nie |
| `jezyk-i-zwroty.md` | H3 | tak | nie na pierwszym etapie |

## Uwagi szczególne do `wycieczki.md`

Plik ma najgłębszą strukturę — do H5 — i powinien być traktowany jako główny test skrajnego przypadku.

Dwa występujące nagłówki H5 mają różny charakter:

- „Hotel Sidi Idriss – wnętrze domu Luke’a z „Gwiezdnych wojen”” jest uzasadnionym, bardziej szczegółowym podtematem Matmaty;
- „Ciekawostka – skąd Tatooine w „Gwiezdnych wojnach”” ma charakter pobocznej ciekawostki i można później rozważyć przedstawienie go jako wyróżnionego bloku zamiast nagłówka.

Nie jest to jednak pilna wada semantyczna.

## Pliki przewidywane do późniejszego wdrożenia

Po osobnym zatwierdzeniu implementacji podstawowy wariant prawdopodobnie obejmie:

- `assets/css/style.css`;
- `_config.yml`;
- nowy `_includes/page-toc.html`;
- dziewięć tematycznych plików Markdown, w których zostanie wywołany wspólny komponent spisu.

W podstawowym wariancie nie ma potrzeby przebudowywać:

- `_data/navigation.yml`;
- `_layouts/default.html`;
- `index.md` pod kątem lokalnego spisu treści.

Dokumenty techniczne nie powinny być publikowane jako strony przewodnika.

## Proponowany pilotaż

Najlepsze trzy strony testowe:

1. `wycieczki.md` — najdłuższa i najgłębsza struktura, do H5;
2. `lacznosc.md` — liczne zagnieżdżenia H4 i operatorzy;
3. `co-kupic-przed-wyjazdem.md` — krótka strona H2-only, pozwalająca sprawdzić, czy ujednolicony spis i mocne H2 nie będą zbyt ciężkie na prostych stronach.

Jeżeli pilotaż ma objąć tylko dwie strony, najlepszy zestaw to:

- `lacznosc.md`;
- `wycieczki.md`.

## Kolejność późniejszej implementacji

1. Wprowadzić semantyczne tokeny kolorów i style H2–H5.
2. Przygotować współdzielony komponent głównego spisu H2.
3. Uruchomić go tylko na dwóch lub trzech stronach pilotażowych.
4. Sprawdzić wygląd, klawiaturę, czytnik ekranu, 100%, 200%, 400%, wąski ekran i mobile.
5. Skorygować siłę H2/H3/H4 oraz wizualną wagę spisu.
6. Dopiero potem rozszerzyć rozwiązanie na wszystkie dziewięć stron tematycznych.
7. Automatyczne lokalne spisy sekcji zaprojektować i wdrożyć jako osobny etap.
8. Tryb ciemny rozważać dopiero później jako odrębnie zatwierdzoną zmianę.

## Rekomendacja końcowa

Docelowy kierunek:

- bez numerowania nagłówków;
- główny automatyczny spis H2 „Na tej stronie” na każdej stronie tematycznej, ale nie na `index.md`;
- H2 jako najmocniejszy wizualny separator;
- H3 jako poziom wyróżniony głównie linią i typografią;
- H4 jako poziom typograficzny;
- jawny styl H5;
- brak wcinania całej treści podsekcji;
- semantyczne tokeny kolorów;
- lokalne spisy H3 wyłącznie w wybranych rozbudowanych sekcjach i dopiero po pilotażu.

Niniejszy plik dokumentuje rekomendacje. Samo jego dodanie do repozytorium nie oznacza wdrożenia opisanych zmian.
