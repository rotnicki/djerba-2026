---
published: false
---

# Audyt etapu 12 — końcowy audyt całego repozytorium

Stan: **audyt zakończony — końcowy werdykt pozytywny i zatwierdzony 23 sierpnia 2026 r.**

Data audytu: 22 sierpnia 2026 r.

Data zakończenia: 23 sierpnia 2026 r.

Ten plik jest roboczą checklistą techniczną etapu 12 z `PLAN-KONTROLI-REPO.md`. Nie jest częścią publicznego przewodnika dla uczestników i nie powinien być publikowany przez GitHub Pages.

Końcowe warunki zamknięcia audytu zostały spełnione i zatwierdzone 23 sierpnia 2026 r. Jedynym świadomie nierozstrzygniętym punktem organizacyjnym pozostaje 12.3 — godzina zbiórki grupy katowickiej — oznaczona jako `oczekuje na ustalenie`, ponieważ nie znaleziono wiarygodnego potwierdzenia i nie należy jej zgadywać.

## Zasady pracy z checklistą

Dla każdego problemu stosujemy statusy:

- `do zatwierdzenia` — problem wykryty w audycie, ale zmiana nie została jeszcze zatwierdzona;
- `zatwierdzone do poprawy` — zakres zmiany został zaakceptowany;
- `poprawione` — zmiana została zapisana do repozytorium;
- `zweryfikowane` — po zapisie ponownie odczytano plik i potwierdzono poprawność;
- `bez zmiany` — po dodatkowym sprawdzeniu świadomie pozostawiono dotychczasową treść;
- `oczekuje na ustalenie` — brak informacji, której nie wolno zgadywać;
- `zamknięte` — problem nie wymaga dalszych działań w etapie 12.

Przed każdą zmianą pliku należy ponownie pobrać jego aktualną wersję i SHA, wykonać tylko zatwierdzony zakres, a następnie ponownie odczytać plik i sprawdzić wynik.

## Wynik audytu przekrojowego

Nie wykryto problemu krytycznego, który czyniłby przewodnik zasadniczo nierzetelnym lub niebezpiecznym.

Po wykonaniu zatwierdzonych poprawek, ponownej kontroli zmienionych plików, ręcznej walidacji dostępności oraz końcowych przebiegach automatycznego sprawdzania linków nie wykryto problemu wymagającego dalszej poprawki przed zamknięciem etapu 12. Końcowy werdykt gotowości repozytorium jest pozytywny.

## Problemy wymagające rozstrzygnięcia

### 12.1. Granica wieku przy podatku turystycznym

Status: **zweryfikowane**.

Priorytet: **ważny**.

Plik: `pieniadze.md`.

Miejsca:

- sekcja „Najkrócej”;
- sekcja „Ile TND mieć od razu”;
- sekcja „Obowiązkowy podatek turystyczny”.

Problem:

W kilku miejscach zapisano, że podatek w wysokości 12 TND za noc dotyczy „osoby, która ukończyła 12 lat”. W audycie wykryto, że granica wieku wymaga bardziej precyzyjnego sformułowania, ponieważ źródła urzędowe i turystyczne nie używają identycznej polskiej formuły.

Znaczenie praktyczne:

Stawka 12 TND, maksymalnie 10 nocy oraz wyliczenie 84 TND za 7 nocy pozostają prawidłowe. Problem dotyczy osoby znajdującej się dokładnie na granicy wieku 12 lat.

Proponowana poprawka:

Ponownie zweryfikować wyłącznie granicę wieku w źródle pierwotnym i ustalić jedno bezpieczne sformułowanie dla całego `pieniadze.md`, bez zmiany stawki i pozostałych zasad podatku.

Dodatkowa weryfikacja źródłowa: **tak — wykonana przed zatwierdzeniem zmiany**.

Wynik wykonania:

- oficjalne źródło tunezyjskie potwierdziło granicę „powyżej 12 lat”; osoby w wieku 12 lat i młodsze są zwolnione;
- we wszystkich pięciu wykrytych miejscach w `pieniadze.md` usunięto sformułowanie sugerujące objęcie podatkiem osoby dokładnie 12-letniej i zastosowano formę „osoba w wieku powyżej 12 lat” lub jej gramatyczny odpowiednik;
- w głównej sekcji „Obowiązkowy podatek turystyczny” dodano jednoznaczne wyjaśnienie granicy wieku;
- poprawiono opis aktualnej informacji ITAKI na „powyżej 12. roku życia”;
- nie zmieniono stawki 12 TND, wyliczenia 84 TND za 7 nocy ani limitu 10 nocy;
- po zapisie ponownie odczytano `pieniadze.md`; nie pozostało żadne wystąpienie sformułowania „ukończyła 12 lat”, a wszystkie sprawdzone miejsca są ze sobą spójne.

### 12.2. Kompletność informacji o szczepieniach — dur brzuszny i WZW B

Status: **zweryfikowane**.

Priorytet: **ważny**.

Plik: `zdrowie.md`.

Problem:

WZW A jest omówione szczegółowo. WZW B pojawia się głównie przy opisie szczepionki skojarzonej Twinrix, natomiast dur brzuszny nie jest omówiony jako osobne zagadnienie podróżne.

W audycie aktualnych zaleceń medycyny podróży wykryto, że oba zagadnienia powinny co najmniej zostać świadomie ocenione dla wyjazdu do Tunezji, szczególnie przy planowanych wyjazdach poza teren kurortu.

Znaczenie praktyczne:

Nie oznacza to automatycznie obowiązku szczepienia całej grupy. Chodzi o kompletność przewodnika i możliwość podjęcia przez uczestnika świadomej indywidualnej decyzji.

Proponowana poprawka:

Po ponownej weryfikacji aktualnych źródeł polskich i uznanych źródeł medycyny podróży przygotować krótką sekcję „Szczepienia do rozważenia przed podróżą do Tunezji”, obejmującą co najmniej:

- szczepienia rutynowe;
- WZW A;
- WZW B u osób nieuodpornionych;
- dur brzuszny, z uwzględnieniem charakteru pobytu i wyjazdów poza strefę hotelową;
- wyraźne rozróżnienie między zaleceniem medycznym a wymogiem wjazdowym;
- zastrzeżenie, że decyzja zależy od stanu zdrowia, wcześniejszych szczepień i terminu pozostałego do wyjazdu.

Dodatkowa weryfikacja źródłowa: **tak — wykonana przed zatwierdzeniem zmiany**.

Wynik wykonania:

- dodano przed szczegółowym rozdziałem o WZW A krótką sekcję „Szczepienia przed podróżą — najważniejsze informacje”;
- zaznaczono, że przy podróży z Polski do Tunezji nie ma obecnie obowiązkowego szczepienia będącego warunkiem wjazdu i warto sprawdzić aktualność szczepień rutynowych;
- WZW A pozostawiono jako zalecane osobom nieuodpornionym, z odesłaniem do istniejącego szczegółowego materiału;
- dodano samodzielną informację o WZW B dla osób niezaszczepionych lub niepewnych swojego statusu;
- dodano dur brzuszny jako szczepienie do indywidualnego rozważenia, z zachowaniem różnicy między szerszym zaleceniem CDC a bardziej zachowawczym ujęciem NIZP PZH–PIB;
- uwzględniono krótki czas do wyjazdu 31 sierpnia 2026 r. i nie obiecano pełnej ochrony po rozpoczęciu szczepienia tuż przed podróżą;
- dodano źródła NIZP PZH–PIB, GIS i CDC;
- nie przebudowano istniejącego rozdziału o WZW A, preparatach, Twinrixie ani cenach;
- po zapisie ponownie odczytano nową sekcję oraz jej styk z rozdziałem o WZW A i Twinrixie; nie stwierdzono sprzeczności.

### 12.3. Godzina zbiórki grupy katowickiej

Status: **oczekuje na ustalenie**.

Priorytet: **ważny**.

Plik: `praktyczne.md`.

Miejsce: sekcja „Grupa katowicka — Katowice Airport”.

Problem:

W publicznym materiale nadal znajduje się zapis „Godzina zbiórki: do uzupełnienia po potwierdzeniu ustaleń grupy katowickiej”.

Znaczenie praktyczne:

Jest to podstawowa informacja organizacyjna potrzebna w dniu wyjazdu.

Proponowana poprawka:

Najpierw sprawdzić aktualne materiały projektu i ustalenia grupy. Jeśli godzina została już potwierdzona, wpisać ją wraz z punktem spotkania, jeżeli ten również jest znany. Jeśli nie została potwierdzona, nie zgadywać i pozostawić punkt jako oczekujący na ustalenie.

Dodatkowa weryfikacja źródłowa: **nie internetowa — potrzebne ustalenie organizacyjne grupy**.

Wynik weryfikacji:

- sprawdzono aktualny `praktyczne.md`;
- przeszukano odpowiednią korespondencję Gmail dotyczącą Dżerby/Tunezji, Katowic, wylotu i asysty;
- sprawdzono dostępne materiały organizatora, w tym przesłaną umowę, która dotyczy wylotu z Warszawy i dlatego nie stanowi źródła dla grupy katowickiej;
- sprawdzono dostępne materiały Google Drive oraz wcześniejsze ustalenia projektu;
- nie znaleziono wiarygodnego potwierdzenia godziny ani punktu zbiórki;
- świadomie pozostawiono placeholder do czasu uzyskania informacji bezpośrednio od grupy katowickiej;
- potwierdzone informacje o Terminalu A i Punkcie PRM nie zostały potraktowane jako uzgodnione miejsce zbiórki.

`praktyczne.md` pozostawiono bez zmian. Podpunkt 12.3 pozostaje oznaczony jako „oczekuje na ustalenie”; świadomy brak tej niepotwierdzonej informacji nie blokuje zamknięcia etapu 12.

### 12.4. Końcowa kontrola polskiej fonetyki zwrotów

Status: **zweryfikowane**.

Priorytet: **redakcyjny/techniczny**.

Plik: `jezyk-i-zwroty.md`.

Problem:

Dokument sam zawiera sekcję „Do sprawdzenia przed ostatecznym wydrukiem lub publikacją ściągi”, obejmującą odsłuchanie kluczowych zwrotów u rodzimych użytkowników i ewentualną korektę polskiej fonetyki.

Audyt nie wykrył jednej konkretnej rażącej pomyłki, ale ten zadeklarowany etap kontroli jakości nie został jeszcze formalnie wykonany.

Znaczenie praktyczne:

Największe znaczenie mają zwroty awaryjne oraz dotyczące pomocy osobom niewidomym.

Proponowana poprawka:

Przeprowadzić punktową kontrolę najważniejszych zwrotów, w szczególności:

- powitanie;
- podziękowanie;
- pytanie o cenę;
- odmowa;
- prośba o pomoc;
- potrzeba lekarza;
- informacja „jestem osobą niewidomą”;
- prośba o podanie ramienia;
- ostrzeżenie o stopniu.

Po wykonaniu kontroli usunąć lub zaktualizować wykonane pozycje z listy „Do sprawdzenia przed ostatecznym wydrukiem lub publikacją ściągi”.

Dodatkowa weryfikacja źródłowa: **tak — wykonana punktowo**.

Wynik wykonania:

- wykonano punktową kontrolę kluczowych zwrotów tunezyjskich i francuskich;
- wykorzystano źródła zawierające transliteracje, zapis IPA oraz dostępne nagrania rodzimych użytkowników;
- jedyną zatwierdzoną korektą była polska wymowa francuskiego `médecin`: `medesę` → `medsę` w zwrocie `J'ai besoin d'un médecin`;
- pozostałe sprawdzone zapisy uznano za poprawne lub akceptowalne dla praktycznej polskiej ściągi i pozostawiono bez zmian;
- oznaczenie `lang="fr"` przy poprawionym zwrocie oraz oznaczenia `lang="ar-TN"` i `dir="rtl"` przy arabskich oryginałach pozostawiono bez zmian;
- z sekcji „Do sprawdzenia przed ostatecznym wydrukiem lub publikacją ściągi” usunięto wykonany punkt o odsłuchaniu kluczowych zwrotów i ewentualnej korekcie fonetyki; pozostałe pozycje listy pozostawiono bez zmian;
- po zapisie ponownie odczytano poprawiony zwrot, końcową listę kontrolną i oznaczenia językowe; nie stwierdzono innych zmian fonetyki ani treści.

## Końcowe walidacje techniczne

### 12.T1. Test wyrenderowanej GitHub Pages klawiaturą i czytnikiem ekranu

Status: **zweryfikowane**.

Priorytet: **ważny technicznie przed zamknięciem etapu 12**.

Sprawdzenie statycznego kodu potwierdziło poprawne podstawy dostępności, w tym:

- główny język strony `lang="pl"`;
- semantyczne `header`, `nav`, `main` i `footer`;
- link „Przejdź do treści”;
- `aria-current="page"` w nawigacji;
- widoczny styl fokusu;
- responsywną nawigację;
- lokalne oznaczenia `lang="fr"` i `lang="ar-TN"` oraz `dir="rtl"` w materiale językowym.

Wynik ręcznej walidacji na wyrenderowanej GitHub Pages:

- skip link: **OK**;
- nagłówki: **OK**;
- landmarki: **OK**;
- kolejność Tab: **OK**;
- francuski `lang`: **OK**;
- arabski `lang` i RTL: **OK**.

W analizie kodu nie wykryto również mechanizmu powodującego problem z reflow przy powiększeniu; zmiany techniczne nie były potrzebne.

Podczas testu użytkownik zwrócił uwagę, że publiczny `jezyk-i-zwroty.md` zawierał techniczną sekcję „Dostępność i oznaczenia języka na WWW”, która nie była potrzebna uczestnikowi korzystającemu z przewodnika. Po zatwierdzeniu:

- usunięto wyłącznie tę techniczną sekcję z publicznego materiału;
- zachowano wszystkie istniejące atrybuty `lang="fr"`, `lang="ar-TN"` i `dir="rtl"` przy samych zwrotach;
- w `README.md` zaktualizowano krótki opis implementacji, usuwając nieaktualne sformułowanie o przyszłej konwersji do HTML i opisując obecny stan GitHub Pages;
- po zapisach sprawdzono diffy obu plików; nie stwierdzono innych zmian w zwrotach, fonetyce ani treści publicznego przewodnika.

### 12.T2. Wynik automatycznego sprawdzania linków

Status: **zweryfikowane**.

Priorytet: **techniczny**.

Workflow `.github/workflows/check-links.yml` sprawdza pliki Markdown i HTML przez Lychee po pushu na `master`, przy pull requestach, ręcznie i cyklicznie.

Wcześniejszy udany przebieg po uporządkowaniu wyjątków:

- przebieg `Check links`: `32622197444`;
- SHA sprawdzonego `master`: `af770fd6fbda40a497a000f5d5dcab2c94d2509e`;
- Lychee: **439 sprawdzeń**, **249 unikalnych URL-i**, **360 poprawnych**, **6 przekierowań**, **79 wyłączonych**, **0 błędów**, **0 timeoutów**.

W toku walidacji wcześniejsze błędy rozdzielono na rzeczywisty nieaktualny link DLI oraz techniczne ograniczenia automatycznego sprawdzania zewnętrznych serwisów, m.in. blokady 403/429 i problemy TLS. Nieaktualne źródło DLI zastąpiono aktualnym oficjalnym źródłem. Pozostałe wyjątki dodawano dopiero po ręcznej, niezależnej weryfikacji konkretnych adresów i możliwie wąsko, bez globalnego `insecure` ani globalnego akceptowania kodów 403, 404 lub 429.

Po końcowej korekcie daty strony startowej wykonano ponowną kontrolę aktualnego `master`:

- końcowy run: `32622919920`;
- próba: **3**;
- job `Lychee`: `97155639994`;
- SHA sprawdzonego `master`: `18ca0111795d5ef228bb531adad10b98de52ad8b`;
- Lychee: **439 sprawdzeń**, **249 unikalnych URL-i**, **360 poprawnych**, **6 przekierowań**, **79 wyłączonych**, **0 timeoutów**, **0 błędów**;
- job `Lychee` oraz krok `Check Markdown and HTML links` zakończyły się wynikiem `success`.

Dwie wcześniejsze próby tego samego runu kończyły się wyłącznie timeoutami zewnętrznych serwisów przy **0 rzeczywistych błędów linków**. Timeouty były przejściowe i zniknęły w trzeciej próbie bez jakiejkolwiek zmiany plików lub konfiguracji repozytorium.

Końcowy przebieg dla aktualnego stanu repozytorium jest zielony. Walidacja 12.T2 jest zakończona.

## Końcowa kontrola po wszystkich zatwierdzonych poprawkach

Po zakończeniu poprawek wykonano ponowną kontrolę aktualnego repozytorium.

- potwierdzono spójność zmienionych plików i najważniejszych informacji między dokumentami;
- ponownie sprawdzono strukturę nawigacji i odsyłacze wewnętrzne;
- potwierdzono, że po wcześniejszym zielonym przebiegu link checkera późniejszy zapis `AUDYT-ETAP-12.md` nie zmienił publicznej treści ani konfiguracji;
- wykryto jedną drobną nieścisłość redakcyjną na stronie startowej: `index.md` nadal podawał „Ostatnia aktualizacja: 22 sierpnia 2026 r.” mimo punktowych aktualizacji publicznych materiałów 23 sierpnia;
- po zatwierdzeniu zmieniono w `index.md` wyłącznie tę datę na **23 sierpnia 2026 r.**; commit: `18ca0111795d5ef228bb531adad10b98de52ad8b`;
- nie zmieniono dat „Stan weryfikacji” w poszczególnych dokumentach, ponieważ odnoszą się one do ich kompleksowej weryfikacji;
- końcowy przebieg `Check links` dla commitu `18ca0111795d5ef228bb531adad10b98de52ad8b` zakończył się sukcesem w próbie 3 runu `32622919920`.

Końcowy werdykt: **repozytorium jest gotowe do zakończenia etapu 12**. Nie wykryto problemu wymagającego kolejnej poprawki przed zamknięciem audytu. Punkt 12.3 pozostaje świadomie oznaczony jako `oczekuje na ustalenie` i powinien zostać uzupełniony dopiero po otrzymaniu wiarygodnego potwierdzenia godziny zbiórki grupy katowickiej.

## Elementy sprawdzone i niewymagające obecnie zmian

Na podstawie audytu całego repozytorium nie wymagają obecnie ponownej przebudowy:

- podział dokumentów na pliki kanoniczne;
- ogólna struktura strony i nawigacji;
- rozdzielenie `README.md` jako dokumentacji repozytorium od `index.md` jako publicznej strony startowej;
- wyłączenie `README.md` i `PLAN-KONTROLI-REPO.md` z GitHub Pages;
- termin wyjazdu 31 sierpnia–7 września 2026 r.;
- 7 nocy pobytu;
- Club Palm Azur i pobyt All Inclusive;
- robocze grupowe założenie około 150 EUR na osobę na fakultety, wyraźnie oddzielone od oficjalnych cen;
- stawka podatku turystycznego 12 TND za noc i wyliczenie 84 TND za 7 nocy — z zastrzeżeniem problemu 12.1 dotyczącego granicy wieku;
- podstawowe zasady paszportowe i wizowe dla naszego pobytu;
- procedura bagażowa i PIR;
- podstawowe limity bagażu Enter Air z zachowawczym przyjęciem bardziej restrykcyjnego wymiaru bagażu podręcznego;
- zasady dotyczące powerbanków i płynów;
- struktura materiału zdrowotnego, ORS/DPN, Enterolu i loperamidu;
- ochrona przeciwsłoneczna, ochrona przed owadami, kontakt ze zwierzętami i bezpieczeństwo w morzu;
- rozróżnienie między polską kartą SIM, podróżną eSIM, Wi-Fi Calling i WhatsAppem;
- zasada weryfikowania konkretnej marki, taryfy i telefonu przy Wi-Fi Calling;
- rozróżnienie poszczególnych ofert i organizatorów wycieczek;
- zasada uzyskania dokładnej trasy przed wyjazdami na południe Tunezji i porównania jej z aktualnymi ostrzeżeniami;
- rozróżnienie wycieczki organizatora od osobnej umowy z lokalnym dostawcą;
- oznaczenia językowe w `jezyk-i-zwroty.md`;
- podstawowa dostępność semantyczna layoutu i CSS, potwierdzona walidacją 12.T1.

## Drobne poprawki opcjonalne

### README — opis przyszłej konwersji do HTML

Status: **wykonane podczas 12.T1**.

Priorytet: **redakcyjny**.

Nieaktualne sformułowanie sugerujące przyszłą konwersję materiałów do HTML zostało zastąpione krótkim opisem obecnej implementacji GitHub Pages. README wskazuje teraz, że główny język strony to polski, francuskie fragmenty mają `lang="fr"`, a arabskie oryginały `lang="ar-TN"` i `dir="rtl"`.

## Warunki zamknięcia etapu 12

Wszystkie warunki zamknięcia etapu 12 zostały spełnione i zatwierdzone:

- [x] problem 12.1 został rozstrzygnięty, poprawiony i zweryfikowany;
- [x] problem 12.2 został rozstrzygnięty, poprawiony i zweryfikowany;
- [x] problem 12.3 został świadomie pozostawiony jako `oczekuje na ustalenie`, ponieważ grupa nadal nie ma wiarygodnie potwierdzonej godziny zbiórki;
- [x] problem 12.4 został wykonany i zweryfikowany;
- [x] walidacja 12.T1 została wykonana i jej wynik zapisany;
- [x] walidacja 12.T2 została wykonana i jej wynik zapisany;
- [x] po wszystkich zatwierdzonych zmianach ponownie sprawdzono spójność zmienionych plików;
- [x] przedstawiono końcowy pozytywny werdykt gotowości publikacji;
- [x] użytkownik 23 sierpnia 2026 r. wyraźnie zatwierdził zakończenie etapu 12.

Po tym zatwierdzeniu status etapu 12 w `PLAN-KONTROLI-REPO.md` powinien zostać zmieniony osobnym zapisem, bez zmian w publicznych materiałach przewodnika.
