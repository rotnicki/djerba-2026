---
published: false
---

# Audyt etapu 12 — końcowy audyt całego repozytorium

Stan: **audyt wykonany, poprawki i walidacje końcowe niezatwierdzone**.

Data audytu: 22 sierpnia 2026 r.

Ten plik jest roboczą checklistą techniczną etapu 12 z `PLAN-KONTROLI-REPO.md`. Nie jest częścią publicznego przewodnika dla uczestników i nie powinien być publikowany przez GitHub Pages.

Etap 12 pozostaje otwarty do czasu:

1. rozstrzygnięcia i wykonania zatwierdzonych poprawek;
2. ponownej kontroli zmienionych plików;
3. wykonania końcowych walidacji technicznych;
4. zatwierdzenia końcowego werdyktu;
5. osobnego polecenia oznaczającego etap 12 jako zakończony w `PLAN-KONTROLI-REPO.md`.

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

Publikacja jest blisko wersji gotowej, ale etap 12 nie powinien być jeszcze zamykany. Do rozstrzygnięcia pozostały trzy ważne problemy treściowe lub organizacyjne, jedna końcowa kontrola jakości językowej oraz dwie walidacje techniczne.

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

`praktyczne.md` pozostawiono bez zmian. Podpunkt 12.3 pozostaje otwarty ze statusem „oczekuje na ustalenie”.

### 12.4. Końcowa kontrola polskiej fonetyki zwrotów

Status: **do zatwierdzenia**.

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

Dodatkowa weryfikacja źródłowa: **tak — punktowa, najlepiej z wiarygodnym materiałem audio lub rodzimym użytkownikiem języka**.

## Końcowe walidacje techniczne

### 12.T1. Test wyrenderowanej GitHub Pages klawiaturą i czytnikiem ekranu

Status: **do wykonania**.

Priorytet: **ważny technicznie przed zamknięciem etapu 12**.

Sprawdzenie statycznego kodu wykazało poprawne podstawy dostępności, w tym:

- główny język strony `lang="pl"`;
- semantyczne `header`, `nav`, `main` i `footer`;
- link „Przejdź do treści”;
- `aria-current="page"` w nawigacji;
- widoczny styl fokusu;
- responsywną nawigację;
- lokalne oznaczenia `lang="fr"` i `lang="ar-TN"` oraz `dir="rtl"` w materiale językowym.

Nie wykonano jednak pełnego rzeczywistego testu wyrenderowanej strony z klawiaturą i czytnikiem ekranu.

Do wykonania:

- przejście całej nawigacji samą klawiaturą;
- sprawdzenie działania skip linku;
- sprawdzenie kolejności fokusu;
- test przy powiększeniu co najmniej 200%;
- test nagłówków, landmarków i listy linków czytnikiem ekranu;
- sprawdzenie przełączania wymowy dla fragmentów francuskich i arabskich;
- sprawdzenie zachowania tekstu arabskiego z `dir="rtl"`.

Zmian technicznych nie wprowadzać profilaktycznie. Wprowadzać je wyłącznie po wykryciu konkretnego problemu w rzeczywistym teście.

### 12.T2. Wynik automatycznego sprawdzania linków

Status: **do wykonania**.

Priorytet: **techniczny**.

Workflow `.github/workflows/check-links.yml` jest skonfigurowany do sprawdzania plików Markdown i HTML przez Lychee po pushu na `master`, przy pull requestach, ręcznie i cyklicznie.

W trakcie audytu nie udało się wiarygodnie potwierdzić wyniku najnowszego przebiegu po ostatnim stanie `master`.

Do wykonania:

- potwierdzić wynik najnowszego `Check links` dla aktualnego `master`;
- jeśli przebieg jest zielony — oznaczyć walidację jako zakończoną;
- jeśli wykryto błędy — przeanalizować każdy wskazany link i przed zmianą przedstawić konkretną propozycję poprawki.

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
- podstawowa dostępność semantyczna layoutu i CSS, z zastrzeżeniem walidacji 12.T1.

## Drobne poprawki opcjonalne

### README — opis przyszłej konwersji do HTML

Status: **opcjonalne**.

Priorytet: **redakcyjny**.

`README.md` zawiera jeszcze sformułowania sugerujące, że oznaczenia lokalnych zmian języka będą potrzebne „przy przyszłej konwersji materiałów do HTML lub publikacji na stronie internetowej”. Strona GitHub Pages już istnieje, a mechanizm oznaczeń językowych został wdrożony.

Można w przyszłości zaktualizować ten fragment tak, aby opisywał obecny stan, ale nie jest to warunek gotowości przewodnika.

## Warunki zamknięcia etapu 12

Etap 12 można przedstawić do końcowego zatwierdzenia dopiero wtedy, gdy:

- [ ] problem 12.1 został rozstrzygnięty i, jeśli zatwierdzono zmianę, poprawiony oraz zweryfikowany;
- [ ] problem 12.2 został rozstrzygnięty i, jeśli zatwierdzono zmianę, poprawiony oraz zweryfikowany;
- [ ] problem 12.3 został rozwiązany albo świadomie pozostawiony jako oczekujący, jeżeli grupa nadal nie zna godziny;
- [ ] problem 12.4 został wykonany albo świadomie uznany za niewymagany przed wyjazdem;
- [ ] walidacja 12.T1 została wykonana i jej wynik zapisany;
- [ ] walidacja 12.T2 została wykonana i jej wynik zapisany;
- [ ] po wszystkich zatwierdzonych zmianach ponownie sprawdzono spójność zmienionych plików;
- [ ] przedstawiono końcowy werdykt gotowości publikacji;
- [ ] użytkownik wyraźnie zatwierdził zakończenie etapu 12.

Dopiero po ostatnim punkcie należy osobnym zapisem zmienić status etapu 12 w `PLAN-KONTROLI-REPO.md`.