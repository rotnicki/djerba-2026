# Audyt i plan przebudowy materiałów o wycieczkach

Status: **audyt zakończony 24 sierpnia 2026 r.; wyniki i ustalenia zapisane, przebudowa nie została jeszcze rozpoczęta**.

Punkt odniesienia: gałąź `master` w commicie `e2230bf36bdeed6cc34cff81c97d70609ec530a4` (`Popraw etykiety obu map`).

Ten dokument zapisuje wyniki pełnego audytu publicznej strony `wycieczki.md`, rekomendacje dotyczące jej przebudowy, decyzje podjęte po audycie oraz kwestie wymagające ostatecznego zatwierdzenia. Jest materiałem technicznym i nie jest publikowany w GitHub Pages.

Na etapie audytu nie zmieniono publicznej treści, nawigacji, stylów, map ani konfiguracji strony.

## Zakres audytu

Przeczytano i porównano w szczególności:

- pełną treść `wycieczki.md`;
- obie wdrożone mapy SVG i ich tekstowe odpowiedniki;
- dokumentację w `techniczne/mapy/`;
- `_layouts/default.html`;
- `assets/css/style.css`;
- `_data/navigation.yml`;
- `_config.yml`;
- `README.md`, `index.md` oraz powiązane audyty i plany techniczne.

Audyt miał odpowiedzieć przede wszystkim na pytanie, czy materiał nadal skutecznie pomaga uczestnikowi zrozumieć możliwości, porównać wycieczki i podjąć decyzję, bez utraty szczegółowych i sprawdzonych informacji.

## Stan obecny

Plik `wycieczki.md` ma:

- około 8 300 słów;
- 1 044 wiersze;
- 107 odnośników;
- 114 nagłówków:
  - 1 nagłówek H1;
  - 10 nagłówków H2;
  - 40 nagłówków H3;
  - 61 nagłówków H4;
  - 2 nagłówki H5;
- dwie mapy SVG osadzone inline;
- dwie numerowane legendy i rozbudowane tekstowe opisy relacji przestrzennych;
- brak tabel porównawczych.

Szczegółowa sekcja porównująca programy rozpoczyna się dopiero po około 4 700 słowach. Wcześniej użytkownik przechodzi przez szybki wybór, instrukcję korzystania z przewodnika, bezpieczeństwo, słownik i cały Atlas miejsc liczący ponad 3 200 słów.

## Ocena ogólna

Materiał jest rzetelnym i dobrze udokumentowanym kompendium, ale tylko częściowo spełnia funkcję szybkiego przewodnika decyzyjnego.

W jednym dokumencie połączono cztery odrębne funkcje:

1. pomoc w wyborze rodzaju wycieczki;
2. Atlas miejsc i orientację przestrzenną;
3. katalog programów, cen i organizatorów;
4. zasady bezpieczeństwa, dostępności i organizacji wycieczek dla grupy.

Najważniejszym problemem nie jest nadmiar niepotrzebnych faktów. Jest nim kolejność, rozproszenie informacji decyzyjnych i konieczność przechodzenia przez kilka warstw szczegółów podczas wykonywania prostego zadania porównawczego.

## Najważniejsze problemy

### Dwie częściowo powtarzające się warstwy wprowadzające

Sekcje `Szybki wybór dla naszej grupy` i `Najkrótsza orientacja – jakie są główne rodzaje wycieczek` realizują zbliżony cel. Powinny zostać połączone w jedną spójną warstwę otwierającą.

### Atlas oddziela wstępny wybór od właściwego porównania

Atlas jest potrzebny i wartościowy, ale obecnie znajduje się przed pełnym porównaniem ofert. Użytkownik zainteresowany np. różnicą między dwiema jednodniowymi wycieczkami na Saharę musi przejść przez opisy wszystkich miejsc.

### Brak porównania równoległego

Oferty są opisywane kolejno w akapitach. Aby je porównać, użytkownik musi pamiętać ceny, programy, język prowadzenia, świadczenia i niewiadome z kilku odległych części dokumentu.

### Zbyt długa lista nagłówków

Hierarchia H1–H5 jest formalnie logiczna i nie pomija poziomów, ale 114 nagłówków tworzy bardzo długą listę w rotorze VoiceOver. Problemem jest liczba i drobiazgowość nagłówków, a nie podstawowy błąd semantyczny.

### Powtarzanie tych samych wyjaśnień

Najczęściej powtarzają się:

- różnica między Ksar Ghilane i Douz;
- znaczenie polskojęzycznego prowadzenia;
- brak ustalonego formalnego organizatora Anety i Cesara;
- potrzeby grupy 18 osób;
- przejrzystość przystanków handlowych;
- ubezpieczenie quadów i jazdy na wielbłądzie;
- charakterystyki miejsc obecne zarówno w Atlasie, jak i przy programach.

Krótkie przypomnienia mogą pozostać, ale pełne wyjaśnienie każdego zagadnienia powinno mieć jedno miejsce kanoniczne.

## Treści, które trzeba zachować

Bez względu na wybrany wariant należy zachować:

- rozróżnienie Ksar Ghilane i Douz;
- wyjaśnienie relacji Tataouine–Tatooine;
- ostrożne oznaczanie potwierdzonych i niepotwierdzonych lokacji filmowych;
- ostrzeżenie, że określenie `słone jezioro` nie musi oznaczać Chott el-Jerid;
- informację o sezonowości flamingów na Ras Rmel;
- daty weryfikacji cen i programów;
- jawne oznaczenie niewiadomych i informacji wymagających potwierdzenia;
- rozróżnienie sprzedawcy, wykonawcy i formalnego organizatora;
- zasady dotyczące quadów, wielbłądów, ubezpieczenia i komunikatów MSZ/Odyseusza;
- potrzeby osób niewidomych i słabowidzących;
- sensoryczne znaczenie miejsc i aktywności;
- skalę dojazdu zamiast pozornie dokładnych czasów przejazdu;
- wzór zapytania dla 18-osobowej grupy;
- obie mapy, ich legendy, opisy przestrzenne i atrybucję OpenStreetMap;
- stałe krótkie etykiety miejsc;
- źródła przy twierdzeniach spornych i szczególnie ważnych.

## Zalecane przeniesienia i skróty

| Obecny element | Zalecane działanie |
| --- | --- |
| `Szybki wybór` i `Najkrótsza orientacja` | połączyć w jedną warstwę otwierającą |
| długa instrukcja korzystania z przewodnika | skrócić do kilku zasad |
| słownik pojęć | przenieść do Atlasu miejsc |
| cały Atlas przed porównaniem programów | przenieść na osobną stronę |
| informacje `Występuje m.in. w programach` przy miejscach | usunąć z Atlasu i utrzymywać przy ofertach |
| pełne profile organizatorów powtarzane przy programach | utrzymywać na stronie ofert |
| powtarzane uwagi o dostępności grupy | zebrać w jednej głównej sekcji i pozostawić krótkie ostrzeżenia przy konkretnych trasach |
| powtarzane wyjaśnienia o przystankach handlowych | zachować jeden pełny opis i krótkie pola w porównaniach |
| lista źródeł powtarzająca odnośniki podane wcześniej | ograniczyć do źródeł rzeczywiście przekrojowych |
| H5 o pochodzeniu nazwy Tatooine | przedstawić jako notę lub zwykły akapit |
| publiczna zapowiedź dodania map w przyszłości | usunąć lub zaktualizować, ponieważ obie mapy są wdrożone |

Nie należy usuwać zweryfikowanych opisów miejsc ani szczegółów ofert tylko w celu skrócenia strony. Powinny zostać przeniesione do właściwej warstwy materiału.

## Warianty architektury

### Jedna przebudowana strona

Zalety:

- jeden adres i jedno wyszukiwanie w dokumencie;
- łatwiejsze zachowanie obecnych kotwic;
- wszystkie szczegóły dostępne bez przechodzenia między stronami.

Wady:

- nadal bardzo długa strona;
- długa lista nagłówków w VoiceOver;
- Atlas i katalog ofert nadal konkurują z funkcją decyzyjną;
- większe ryzyko ponownego narastania treści.

### Dwie strony

Wariant `wybór i oferty + Atlas` oddzieliłby mapy i opisy miejsc, ale główna strona z pełnym katalogiem ofert nadal byłaby długa.

### Trzy strony łącznie

Rekomendowany wariant obejmuje:

1. przebudowaną obecną stronę `wycieczki.md` — szybki wybór i porównanie;
2. nową stronę `atlas-miejsc.md` — obie mapy i pełne opisy miejsc;
3. nową stronę `oferty-wycieczek.md` — szczegółowe programy, ceny i organizatorów.

Są to trzy strony łącznie, czyli dwie nowe strony oraz przebudowa obecnej.

## Ustalenia potwierdzone po audycie

Użytkownik potwierdził następujące założenia organizacyjne:

- późniejsze wdrożenie ma zostać wykonane możliwie jednym skoordynowanym przebiegiem, a nie jako seria częściowo opublikowanych etapów;
- wszystkie trzy strony dotyczące wycieczek mają być dostępne bezpośrednio w głównej nawigacji;
- użytkownik nie powinien być zmuszony do wejścia najpierw na stronę `Wycieczki`, aby dopiero z niej dotrzeć do Atlasu lub szczegółowych ofert;
- kolejność nowych pozycji trzeba rozpatrywać razem z kolejnością całej głównej nawigacji;
- tabele mogą zostać użyte tylko wtedy, gdy będą proste, rzeczywiście pomocne w porównaniu i poprawnie oznaczone semantycznie.

## Proponowana główna nawigacja

Poniższa kolejność jest rekomendacją do ostatecznego zatwierdzenia podczas wdrożenia:

1. Start;
2. Praktyczne informacje;
3. Zdrowie;
4. Co zabrać;
5. Co kupić przed wyjazdem;
6. Łączność;
7. Pieniądze i płatności;
8. Wycieczki – wybór;
9. Atlas miejsc;
10. Oferty wycieczek;
11. Kultura i zwyczaje;
12. Język i zwroty.

Kolejność trzech stron odzwierciedla trzy zadania użytkownika:

1. wybranie rodzaju wycieczki;
2. zrozumienie miejsc, nazw, odległości i map;
3. szczegółowe porównanie ofert handlowych.

Jeżeli wszystkie trzy strony znajdą się w głównej nawigacji, dodatkowa rozbudowana nawigacja lokalna nie jest konieczna. W treści powinny jednak występować kontekstowe odnośniki, np. `Zobacz miejsce w Atlasie` i `Porównaj szczegółowe oferty`.

## Proponowana struktura stron

### Strona decyzyjna `wycieczki.md`

- H1 `Wycieczki – porównanie i wybór`;
- H2 `Najważniejsze wnioski dla naszej grupy`;
- H2 `Porównanie rodzajów wycieczek`;
- H3 dla objazdu Dżerby, jednodniowej Sahary, Tataouine i ksarów, lekkich propozycji oraz Sahary z noclegiem;
- H2 `Różnice, których nie widać w nazwie`;
- H3 dla Ksar Ghilane i Douz, Tataouine i Tatooine, Ras Rmel oraz słonych jezior;
- H2 `Dostępność i wysiłek dla naszej grupy`;
- H2 `Przed zakupem wycieczki`;
- H3 dla programu i ceny, organizatora i ubezpieczenia oraz warunków grupowych;
- H2 `Wstępny plan wyboru i negocjacji`;
- H2 `Szczegółowe materiały`.

### Strona `atlas-miejsc.md`

- H1 `Atlas miejsc i mapy`;
- H2 `Jak korzystać z Atlasu`;
- H2 `Dżerba – mapa i relacje przestrzenne`;
- H3 dla poszczególnych miejsc na Dżerbie;
- H2 `Wyjazd z Dżerby – mapa południa i relacje przestrzenne`;
- H2 `Tataouine i góry Dahar`;
- H3 dla poszczególnych miejsc regionu;
- H2 `Sahara`;
- H3 dla Ksar Ghilane, Douz, Chott el-Jerid oraz Tozeur i górskich oaz;
- H2 `Słownik pojęć`;
- H2 `Źródła Atlasu`.

### Strona `oferty-wycieczek.md`

- H1 `Oferty wycieczek – szczegółowe porównanie`;
- H2 `Jak czytać ceny i programy`;
- osobne H2 dla kolejnych rodzajów wycieczek;
- H2 `Organizatorzy i odpowiedzialność`;
- H3 dla poszczególnych sprzedawców i organizatorów;
- H2 `Oferta dla grupy 18 osób`;
- H2 `Pytania do zadania na miejscu`;
- H2 `Źródła i data weryfikacji`.

Docelowo wszystkie trzy strony powinny zatrzymywać hierarchię na H3. Nie przewiduje się potrzeby używania H4 i H5.

## Zasady stosowania tabel

Tabela nie jest z założenia niedostępna. Przy prawidłowej semantyce może być lepszym narzędziem porównawczym niż seria długich list, ponieważ użytkownik czytnika ekranu może poruszać się między komórkami i korzystać z nagłówków kolumn i wierszy.

### Gdzie stosować tabele

Małe tabele są rekomendowane do:

- porównania rodzajów wycieczek;
- porównania ofert dla jednego rodzaju wycieczki;
- zestawienia ceny, głównych punktów programu i najważniejszych niewiadomych;
- pokazania różnic między Ksar Ghilane i Douz.

### Gdzie nie stosować tabel

W formie list i zwykłego tekstu powinny pozostać:

- legendy map;
- opisy relacji przestrzennych;
- pełne opisy miejsc;
- checklisty i pytania;
- zasady bezpieczeństwa i dostępności;
- profile organizatorów;
- źródła.

### Wymagania semantyczne i użytkowe

Każda tabela publiczna powinna:

- mieć widoczny element `caption`;
- mieć nagłówki kolumn jako `th scope="col"`;
- używać nazwy wariantu lub oferty jako nagłówka wiersza `th scope="row"`;
- mieć najwyżej około czterech kolumn;
- nie używać scalonych ani pustych komórek;
- zawierać krótkie dane porównawcze, a nie wielkie akapity;
- dotyczyć jednego rodzaju wycieczki zamiast łączyć wszystkie oferty w jedną macierz;
- korzystać z natywnego HTML bez zbędnych ról ARIA;
- zachować dostępne przewijanie poziome, jeżeli będzie konieczne na małym ekranie;
- zostać sprawdzona w VoiceOver z Safari na Macu i iPhonie oraz przy powiększeniu 200% i 400%.

Ze względu na potrzebę kontroli `caption`, nagłówków wierszy i atrybutów `scope` rekomendowane jest użycie bezpośredniego HTML zamiast polegania wyłącznie na składni tabel Markdown.

Najlepszym rozwiązaniem jest model mieszany: krótka tabela daje szybkie porównanie, a zwykły tekst pod nią wyjaśnia tylko te szczegóły i niepewności, których nie należy wciskać do komórek.

## Sekcje rozwijane

Natywne elementy `details` i `summary` mogą być dostępne, ale nie powinny ukrywać treści potrzebnych do decyzji.

Nie należy w nich umieszczać:

- głównych rekomendacji;
- porównania cen i programów;
- zasad bezpieczeństwa;
- opisów map;
- informacji wymaganych przed zakupem.

Można je później rozważyć jedynie dla pobocznych ciekawostek lub dłuższych wyjaśnień źródłowych. Wymagałoby to stylu fokusu dla `summary` i osobnych testów VoiceOver. Sekcje rozwijane nie są głównym rozwiązaniem problemu długości materiału.

## Mapy i ich dostępność

Obie mapy powinny zostać przeniesione na stronę Atlasu i pozostać tam osadzone tylko raz.

Należy zachować:

- SVG osadzone inline;
- `role="img"`;
- nazwę i opis przez `title`, `desc` i `aria-labelledby`;
- ukrycie surowych warstw mapy przed osobną nawigacją czytnika;
- numerowane legendy w zwykłym HTML;
- tekstowe opisy relacji przestrzennych;
- różne kształty hotelu i atrakcji;
- atrybucję OpenStreetMap;
- tryb jasny, ciemny i wymuszone kolory;
- nazwany i fokusowalny kontener przewijanej mapy.

Nie należy powtarzać tych samych SVG na kilku stronach bez przeprojektowania identyfikatorów. Strona główna wycieczek powinna prowadzić odnośnikami do odpowiednich części Atlasu.

## Linki i kotwice

Przy wdrożeniu należy:

- zachować adres `/wycieczki.html` dla głównej strony decyzyjnej;
- dodać dwie nowe strony do głównej nawigacji;
- nadać najważniejszym sekcjom jawne i stabilne identyfikatory;
- zaktualizować odnośnik techniczny prowadzący obecnie do `wycieczki.html#dżerba`;
- zaktualizować linki z `pieniadze.md`, jeżeli mają prowadzić bezpośrednio do szczegółowych cen;
- sprawdzić wszystkie odnośniki wewnętrzne i zewnętrzne po przeniesieniu treści.

Nie rekomenduje się utrzymywania kilkudziesięciu pustych kotwic dla wszystkich dawnych H3–H5. Najważniejsze kotwice H2 powinny być zachowane lub świadomie przekierowane przez krótkie sekcje prowadzące do nowej strony.

## Wykryte nieaktualności dokumentacji

Podczas audytu stwierdzono:

- publiczna sekcja `Źródła i mapy` w `wycieczki.md` nadal opisuje własne mapy jako rozwiązanie planowane na kolejną wersję, choć obie są już wdrożone;
- `techniczne/wizualizacje/README.md` nadal określa własne mapy jako planowane i niewykonane;
- `techniczne/mapy/mapa-dzerby.md` zawiera starszy zakres kadru oraz starszą sumę wynikowego SVG;
- aktualna suma `_includes/maps/djerba.svg` to `4061bc6669d29115073c113f76142b14e07002967d5a9186562338b61cc4722f`, zgodna z późniejszym dokumentem `techniczne/mapy/kontekst-geograficzny-dzerby.md`.

Te niespójności nie wpływają na bieżące działanie map, ale powinny zostać poprawione podczas jednego całościowego wdrożenia przebudowy.

## Plan jednego całościowego wdrożenia

Po zatwierdzeniu szczegółów należy:

1. ponownie pobrać aktualny `master`;
2. sporządzić mapę przeniesienia każdej części obecnego `wycieczki.md`;
3. utworzyć dwie nowe strony i najpierw przenieść treść bez jej usuwania;
4. przebudować główną stronę decyzyjną;
5. dodać małe dostępne tabele porównawcze;
6. usunąć dopiero potwierdzone powtórzenia;
7. ujednolicić nazwy i krótkie etykiety miejsc;
8. dodać wszystkie trzy strony do głównej nawigacji i zaktualizować stronę startową;
9. poprawić nieaktualną dokumentację map i wizualizacji;
10. zaktualizować linki, kotwice i opisy plików kanonicznych;
11. zbudować stronę lokalnie i sprawdzić wynikowy HTML;
12. wykonać testy automatyczne i ręczne;
13. opublikować dopiero kompletny i sprawdzony zestaw zmian.

Wdrożenie może być prowadzone wewnętrznie w kilku kontrolowanych krokach, ale nie powinno publikować użytkownikom stanu pośredniego z brakującymi stronami lub niespójną nawigacją.

## Wymagane kontrole

- dokładnie jeden H1 na każdej stronie;
- brak pomijania poziomów nagłówków;
- docelowo brak H4 i H5;
- poprawność `caption`, `scope="col"` i `scope="row"` w tabelach;
- czytelność i przewijanie tabel na małych ekranach;
- zgodność obu legend z oznaczeniami map;
- unikatowość identyfikatorów SVG i kotwic HTML;
- VoiceOver z Safari na iPhonie i Macu;
- pomocniczo NVDA;
- klawiatura;
- szerokość około 320 CSS px;
- powiększenie 200% i 400%;
- tryb jasny, ciemny i wymuszone kolory;
- kontrola linków;
- kontrola publikacji GitHub Pages.

## Przewidywany zakres plików

Wariant trzech stron prawdopodobnie będzie wymagał zmiany:

- `wycieczki.md`;
- nowego `atlas-miejsc.md`;
- nowego `oferty-wycieczek.md`;
- `_data/navigation.yml`;
- `assets/css/style.css`;
- `index.md`;
- `README.md`;
- `pieniadze.md`;
- dokumentacji w `techniczne/mapy/`;
- `techniczne/wizualizacje/README.md`;
- niniejszego raportu po wdrożeniu.

Bez zmiany nazw widocznych na mapach nie powinny wymagać modyfikacji:

- `_layouts/default.html`;
- `_config.yml`;
- `_includes/maps/djerba.svg`;
- `_includes/maps/south-tunisia.svg`;
- generatory map.

## Podział rekomendacji według pilności

### Zmiany konieczne

- umieścić szybką orientację i porównanie przed Atlasem i szczegółami;
- połączyć częściowo dublujące się wprowadzenia;
- umożliwić porównanie ofert bez zapamiętywania wielu akapitów;
- ograniczyć liczbę i głębokość nagłówków;
- zachować pełne odpowiedniki tekstowe obu map;
- poprawić nieaktualne informacje o stanie map;
- usuwać powtórzenia dopiero po potwierdzeniu zachowania wszystkich ważnych faktów.

### Zmiany rekomendowane

- podział na trzy strony łącznie;
- bezpośrednia obecność wszystkich trzech stron w głównej nawigacji;
- kilka małych, dostępnych tabel porównawczych;
- zatrzymanie hierarchii na H3;
- przeniesienie słownika do Atlasu;
- przeniesienie pełnych profili organizatorów na stronę ofert;
- jawne i stabilne identyfikatory najważniejszych sekcji;
- aktualizacja dokumentacji technicznej map.

### Zmiany opcjonalne

- natywne sekcje `details` dla pobocznych wyjaśnień po osobnych testach;
- dodatkowe mapy konkretnych tras;
- zdjęcia reprezentujące miejsca;
- wspólny plik danych dla stałych nazw miejsc;
- lokalne spisy treści na nowych stronach, jeżeli po podziale nadal okażą się potrzebne.

## Kwestie do ostatecznego zatwierdzenia

Przed rozpoczęciem przebudowy trzeba jeszcze ostatecznie zatwierdzić:

- dokładne tytuły trzech stron i nazwy dwóch nowych plików;
- pełną kolejność głównej nawigacji;
- ostateczną strukturę H2 i H3;
- zestaw konkretnych tabel oraz ich kolumny;
- sposób zachowania najważniejszych dotychczasowych kotwic;
- czy raport ma być aktualizowany w tym samym commicie co wdrożenie, czy w osobnym końcowym commicie dokumentacyjnym.
