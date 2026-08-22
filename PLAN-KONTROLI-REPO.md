# Plan końcowej kontroli repozytorium

Stan planu: 22 sierpnia 2026 r.

Ten plik jest technicznym planem dalszych prac nad repozytorium `djerba-2026`. Nie jest częścią publicznego przewodnika dla uczestników i powinien pozostać wyłączony z GitHub Pages.

## Zasada pracy

Zmiany wykonujemy małymi etapami, aby nie zepsuć poprawnych informacji ani nie wprowadzić nowych sprzeczności.

Dla każdego etapu obowiązuje kolejność:

1. pobrać z repo aktualną wersję wszystkich plików objętych etapem;
2. sprawdzić aktualne źródła, jeśli informacja zależy od czasu, przepisów, przewoźnika, hotelu, zdrowia, operatora lub organizatora;
3. najpierw przygotować propozycję konkretnych zmian bez zapisywania ich do repo;
4. uzyskać zatwierdzenie zakresu zmian;
5. bezpośrednio przed każdym zapisem ponownie pobrać aktualny SHA danego pliku;
6. wykonać tylko zatwierdzone zmiany;
7. po zapisie ponownie odczytać zmieniony plik i sprawdzić wynik;
8. dopiero po kontroli oznaczyć etap jako zakończony i przejść do następnego.

Nie wykonujemy dużej automatycznej przebudowy wielu dokumentów naraz. Przy redukowaniu dublowania żadna informacja nie może zniknąć przypadkowo: musi pozostać w pliku kanonicznym albo zostać świadomie usunięta jako zbędna lub nieaktualna.

## Kolejność etapów

### 1. Dokumenty i formalności podróży

Status: **zakończony 22 sierpnia 2026 r.**

Zakres:

- `co-zabrac.md`;
- w razie potrzeby `praktyczne.md`.

Do sprawdzenia i uzupełnienia:

- wymagania dotyczące ważności paszportu dla obywatela Polski;
- brak obowiązku wizowego dla naszego pobytu, jeśli nadal aktualny;
- dokumenty podróży i voucher;
- wymaganie Coral dotyczące wydrukowanych dokumentów przy locie czarterowym;
- zalecenie posiadania kopii/skanu paszportu przechowywanego oddzielnie;
- obowiązek ponownego potwierdzenia godziny lotu dzień przed wylotem i dzień przed powrotem.

### 2. Lotniska i asysta PRM

Status: **do wykonania**.

Zakres:

- `praktyczne.md`;
- Warszawa i Katowice.

Cele:

- zachować ustaloną organizację zbiórki grupy;
- oprzeć procedurę PRM przede wszystkim na oficjalnych źródłach lotnisk, przepisach i dokumentach Coral;
- usunąć lub zastąpić źródła nieoficjalne, jeśli są używane do kluczowych twierdzeń;
- nie zmieniać ustaleń grupowych bez wyraźnej potrzeby.

### 3. Hotel i rozmieszczenie pokoi

Status: **do wykonania**.

Zakres: `praktyczne.md`.

Cele:

- oddzielić temat rozmieszczenia pokoi od drobnych upominków;
- oprzeć informację o pokojach obok siebie na warunkach Coral jako na źródle podstawowym;
- jasno zaznaczyć, że jest to życzenie, a nie gwarancja;
- pozostawić relacje podróżnych jedynie jako źródło pomocnicze;
- przed wyjazdem sprawdzić, czy prośba o bliskie pokoje figuruje przy rezerwacji/voucherze.

### 4. Zagubiony lub uszkodzony bagaż

Status: **do wykonania**.

Zakres: `co-zabrac.md` lub `praktyczne.md`, po ocenie najlepszego miejsca.

Dodać krótką procedurę:

- zgłoszenie problemu jeszcze w strefie przylotów;
- Lost & Found / właściwe stanowisko bagażowe;
- uzyskanie i zachowanie raportu PIR;
- zachowanie karty pokładowej i kwitu bagażowego.

### 5. Pieniądze i podatek turystyczny

Status: **do wykonania**.

Zakres: `pieniadze.md`.

Cele:

- zweryfikować granicę wieku dla podatku turystycznego i zapisać ją jednoznacznie;
- ponownie sprawdzić stawkę 12 TND i wyliczenie 84 TND dla 7 nocy;
- upewnić się, że 150 EUR pozostaje aktualnym grupowym założeniem na fakultety;
- usunąć z publicznej treści mylące historyczne założenia, jeśli nie są już potrzebne.

### 6. Zdrowie – brakujące ryzyka

Status: **do wykonania**.

Zakres:

- `zdrowie.md`;
- `co-zabrac.md`;
- `co-kupic-przed-wyjazdem.md`.

Do rozważenia po weryfikacji źródeł:

- repelent przeciw komarom i innym owadom;
- preparat łagodzący ukąszenia;
- unikanie kontaktu z bezpańskimi zwierzętami;
- postępowanie po ugryzieniu lub zadrapaniu;
- ewentualne inne istotne zalecenia zdrowotne wynikające z aktualnych zaleceń dla Tunezji.

### 7. Wycieczki, aktywności i ubezpieczenie

Status: **do wykonania**.

Zakres: `wycieczki.md` i ewentualnie `praktyczne.md`.

Cele:

- przed quadami/ATV i innymi aktywnościami sprawdzać zakres konkretnej polisy;
- wyjaśnić różnicę odpowiedzialności między wycieczką kupioną jako świadczenie organizatora a osobną umową z lokalnym dostawcą;
- przy trasach na południe sprawdzać aktualne komunikaty MSZ/Odyseusza dla konkretnej trasy;
- nie usuwać istniejącego porównania ofert i organizatorów.

### 8. Język i dostępność

Status: **do wykonania**.

Zakres: `jezyk-i-zwroty.md` oraz w razie potrzeby layout/Jekyll.

Cele:

- wdrożyć lokalne oznaczenia `lang` dla francuskiego i arabskiego;
- przy arabskim stosować właściwy kierunek tekstu `dir="rtl"`;
- polską fonetykę pozostawić oznaczoną jako polską;
- zweryfikować najważniejsze zapisy fonetyczne;
- dodać praktyczne zwroty dla osób niewidomych, np. prośbę o podanie ramienia i informację o stopniu/przeszkodzie.

### 9. Redukcja dublowania i pliki kanoniczne

Status: **do wykonania**.

Cele:

- wskazać jeden plik kanoniczny dla każdego większego tematu;
- w innych dokumentach pozostawiać krótkie podsumowanie i link;
- szczególnie uporządkować alkohol, ORS/DPN, ceny preparatów, słońce i wybrane informacje hotelowe;
- nie usuwać treści, dopóki nie zostanie potwierdzone, że jest zachowana w odpowiednim miejscu.

Przykładowe pliki kanoniczne:

- zdrowie i uzasadnienia medyczne → `zdrowie.md`;
- lista pakowania → `co-zabrac.md`;
- konkretne zakupy i ceny produktów → `co-kupic-przed-wyjazdem.md`;
- pieniądze → `pieniadze.md`;
- łączność → `lacznosc.md`;
- wycieczki → `wycieczki.md`.

### 10. Uporządkowanie dużych dokumentów

Status: **do wykonania**.

Najważniejsze:

- `lacznosc.md` – na początku prosty plan działania dla grupy, szczegóły operatorów później;
- `praktyczne.md` – utrzymać funkcję szybkiej ściągi, skrócić dominację szczegółowej instrukcji Odyseusza na wejściu;
- `zdrowie.md` – wyeksponować najważniejsze działania i objawy alarmowe, a szczegóły naukowe pozostawić niżej;
- `wycieczki.md` – zachować szczegółowość, ale poprawić szybkie wnioski decyzyjne na początku.

### 11. Porządki techniczne i redakcyjne

Status: **do wykonania**.

Do sprawdzenia:

- jednolite określenie daty weryfikacji dokumentów;
- tytuły HTML, w tym ewentualne powtarzanie `Dżerba 2026 – Dżerba 2026`;
- usunięcie zbędnych publicznych historii zmian tam, gdzie historię zapewnia Git;
- opis działów na `index.md`;
- automatyczny link checker;
- odsyłacze wewnętrzne;
- martwe i przekierowane linki;
- poprawność nawigacji i nagłówków.

### 12. Końcowy audyt całego repozytorium

Status: **do wykonania**.

Po zakończeniu etapów 1–11 ponownie przeczytać całe repo od początku i sprawdzić:

- spójność techniczną;
- spójność merytoryczną;
- brak sprzecznych liczb, dat i zaleceń;
- brak niepotrzebnego dublowania;
- kompletność informacji przed wyjazdem;
- jakość źródeł;
- czytelność dla uczestnika szukającego informacji w pośpiechu;
- dostępność wyrenderowanej strony GitHub Pages, w tym test klawiaturą i czytnikiem ekranu.

## Najważniejsza zasada bezpieczeństwa zmian

Jeżeli w trakcie pracy pojawi się wątpliwość, czy coś usunąć, przenieść albo zastąpić, **domyślnie zachowujemy istniejącą informację do czasu rozstrzygnięcia**. Lepsza jest chwilowa redundancja niż przypadkowa utrata ważnej treści.

Jeżeli źródła są ze sobą sprzeczne, zapisujemy rozbieżność i jej znaczenie praktyczne zamiast wybierać jedno źródło bez wyjaśnienia.
