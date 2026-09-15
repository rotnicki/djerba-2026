# Transkrypcje nagrań

Ten katalog przechowuje transkrypcje nagrań wykorzystywanych przy opracowywaniu dziennika podróży „Dżerba 2026”. Nagrania źródłowe pozostają poza repozytorium, przede wszystkim na Dropboxie. W repozytorium zapisujemy wyłącznie tekstowe materiały pochodne.

## Zasady

- jedno nagranie źródłowe odpowiada jednemu plikowi transkrypcji w formacie Markdown;
- podstawą identyfikacji jest pełna, oryginalna nazwa nagrania wraz z rozszerzeniem;
- nazwa pliku transkrypcji zachowuje możliwie wiernie nazwę źródła, ale ma rozszerzenie `.md`;
- numer, data i godzina zakodowane w nazwie źródłowej są przepisywane do metadanych transkrypcji;
- data wynikająca wyłącznie z nazwy pliku pozostaje oznaczona jako ustalona z nazwy, dopóki nie zostanie potwierdzona innym źródłem;
- treść transkrypcji zachowujemy oddzielnie od późniejszych notatek, interpretacji i fragmentów włączanych do dziennika;
- fragmentów niezrozumiałych nie zgadujemy — oznaczamy je wraz ze znacznikiem czasu, jeżeli jest dostępny;
- każda późniejsza korekta pozostaje widoczna w historii Git.

## Indeks

Indeks będzie uzupełniany po dodaniu każdej transkrypcji. Dla każdego nagrania podajemy:

- oryginalną nazwę pliku;
- nazwę pliku transkrypcji;
- datę i godzinę nagrania;
- źródło materiału;
- status opracowania;
- powiązanie z dniem lub częścią dziennika.

## Szablon transkrypcji

```markdown
# Transkrypcja nagrania

- Oryginalny plik: `nazwa-pliku.mp3`
- Źródło: Beata
- Data i godzina nagrania: do ustalenia
- Podstawa datowania: nazwa pliku / metadane / treść nagrania
- Status: transkrypcja surowa
- Metoda transkrypcji: do uzupełnienia
- Powiązanie z dziennikiem: do ustalenia

## Transkrypcja

[Treść transkrypcji]

## Miejsca niepewne

- Brak albo lista fragmentów oznaczonych jako niezrozumiałe.

## Uwagi robocze

- Informacje pomocnicze niewchodzące do samej transkrypcji.
```

## Statusy

- **transkrypcja surowa** — tekst nie został jeszcze porównany z nagraniem;
- **częściowo zweryfikowana** — sprawdzono tylko wskazane fragmenty;
- **zweryfikowana** — całość porównano z nagraniem;
- **wykorzystana w dzienniku** — informacje z nagrania zostały opracowane i powiązane z właściwą częścią dziennika.
