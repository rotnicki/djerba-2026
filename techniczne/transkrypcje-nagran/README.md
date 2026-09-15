# Transkrypcje nagrań

Ten katalog przechowuje transkrypcje nagrań wykorzystywanych przy opracowywaniu dziennika podróży „Dżerba 2026”. Nagrania źródłowe pozostają poza repozytorium, przede wszystkim na Dropboxie. W repozytorium zapisujemy wyłącznie tekstowe materiały pochodne.

## Pochodzenie materiałów

- nagrania zostały zapisane jako pliki MP3 za pomocą urządzenia Orion przeznaczonego dla osób niewidomych;
- dokładna nazwa i model urządzenia pozostają do potwierdzenia;
- pierwsze automatyczne transkrypcje powstają na iPhonie w aplikacji określonej roboczo jako „Whisper Transcribe”;
- dokładna nazwa aplikacji i jej producent pozostają do potwierdzenia;
- nagrania pochodzą głównie od Beaty i często rejestrują wypowiedzi przewodnika oraz dźwięki otoczenia;
- aplikacja może zwracać surowy tekst zapisany jednym ciągiem, bez wiarygodnego podziału na zdania, akapity lub rozmówców.

## Zasady

- jedno nagranie źródłowe odpowiada jednemu plikowi transkrypcji w formacie Markdown;
- podstawą identyfikacji jest pełna, oryginalna nazwa nagrania wraz z rozszerzeniem;
- nazwa pliku transkrypcji zachowuje możliwie wiernie nazwę źródła, ale ma rozszerzenie `.md`;
- numer, data i godzina zakodowane w nazwie źródłowej są przepisywane do metadanych transkrypcji;
- data wynikająca wyłącznie z nazwy pliku pozostaje oznaczona jako ustalona z nazwy, dopóki nie zostanie potwierdzona innym źródłem;
- otrzymany tekst zapisujemy najpierw bez przeredagowywania jako transkrypcję surową;
- wersję uporządkowaną przygotowujemy oddzielnie: dodajemy interpunkcję, podział na zdania i akapity oraz poprawiamy oczywiste błędy rozpoznawania mowy, nie dopisując treści, której nie ma w materiale;
- transkrypcję surową zachowujemy także po przygotowaniu wersji uporządkowanej;
- treść transkrypcji zachowujemy oddzielnie od późniejszych notatek, interpretacji i fragmentów włączanych do dziennika;
- fragmentów niezrozumiałych nie zgadujemy — oznaczamy je wraz ze znacznikiem czasu, jeżeli jest dostępny;
- każda późniejsza korekta pozostaje widoczna w historii Git.

## Indeks

Indeks będzie uzupełniany po dodaniu każdej transkrypcji. Dla każdego nagrania podajemy:

- oryginalną nazwę pliku;
- nazwę pliku transkrypcji;
- datę i godzinę nagrania;
- źródło materiału;
- status transkrypcji surowej;
- status wersji uporządkowanej i weryfikacji;
- powiązanie z dniem lub częścią dziennika.

### Dodane transkrypcje

- [`nagranie20260902_1.mp3`](nagranie20260902_1.md) — 2 września 2026, godzina nieustalona; źródło: Beata; transkrypcja surowa, niezweryfikowana; objazd wyspy w stronę Guellali i postój przy meczecie.

## Szablon transkrypcji

```markdown
# Transkrypcja nagrania

- Oryginalny plik: `nazwa-pliku.mp3`
- Źródło nagrania: Beata
- Urządzenie nagrywające: Orion; dokładna nazwa i model do potwierdzenia
- Format źródłowy: MP3
- Data i godzina nagrania: do ustalenia
- Podstawa datowania: nazwa pliku / metadane / treść nagrania
- Narzędzie transkrypcji: „Whisper Transcribe” na iPhonie; dokładna nazwa do potwierdzenia
- Status transkrypcji: surowa
- Status wersji uporządkowanej: nieopracowana
- Powiązanie z dziennikiem: do ustalenia

## Transkrypcja surowa

[Tekst dokładnie w postaci otrzymanej z aplikacji]

## Wersja uporządkowana

[Do przygotowania później bez zmiany znaczenia wypowiedzi]

## Miejsca niepewne

- Brak albo lista fragmentów oznaczonych jako niezrozumiałe.

## Uwagi robocze

- Informacje pomocnicze niewchodzące do samej transkrypcji.
```

## Statusy

- **surowa** — tekst zapisano w postaci otrzymanej z aplikacji;
- **uporządkowana** — dodano interpunkcję i czytelny podział tekstu oraz poprawiono oczywiste błędy, bez porównania całej treści z nagraniem;
- **częściowo zweryfikowana** — tylko wskazane fragmenty porównano z nagraniem;
- **zweryfikowana** — całość porównano z nagraniem;
- **wykorzystana w dzienniku** — informacje z nagrania zostały opracowane i powiązane z właściwą częścią dziennika.
