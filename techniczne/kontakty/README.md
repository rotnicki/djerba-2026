# Kontakty vCard

Ten katalog zawiera jedno źródło danych, generator i testy wizytówek używanych w przewodniku.

## Przyjęty model

- Format: vCard 3.0, UTF-8, zakończenia CRLF.
- Maksymalna długość fizycznego wiersza: 75 oktetów.
- `N:;;;;` pozostaje puste, ponieważ są to instytucje, a nie osoby. Zapobiega to zapisaniu całej nazwy jako imienia.
- `FN` i `ORG` zawierają tę samą krótką polską nazwę użytkową zaczynającą się od `Djerba —`. Test iPhone'a wykazał, że przy pustym `N` system pokazuje `ORG`, a nie `FN`.
- Oficjalna nazwa instytucji pozostaje w źródle danych i — gdy jest potrzebna użytkownikowi — także w `NOTE`.
- Krótkie numery alarmowe używają prostego `TEL`, bez technicznej etykiety `VOICE`.
- `EMAIL;TYPE=INTERNET` i `ADR;TYPE=WORK` występują tylko tam, gdzie mają praktyczne zastosowanie. Pole `EMAIL` nie używa niestandardowej dla vCard 3.0 etykiety `WORK`.
- `NOTE` wyjaśnia zastosowanie numeru; przecinki i średniki są escapowane.
- `CATEGORIES` zostało pominięte, ponieważ importery nie tworzą z niego niezawodnie listy kontaktów. Wspólne wyszukiwanie zapewnia prefiks `Djerba —`.

Publiczna strona udostępnia wyłącznie osiem plików pojedynczych. Test na rzeczywistym iPhonie wykazał, że pojedynczy plik otwiera poprawny podgląd i udostępnia polecenie „Utwórz nowy kontakt”. Plik wielokontaktowy otwarty bezpośrednio ze strony pokazywał tylko pierwszy kontakt, a przekazanie go przez arkusz udostępniania do Kontaktów nie powodowało importu. Dlatego wariant zbiorczy został usunięty, aby nie sugerować użytkownikom niesprawdzonej ścieżki.

## Generowanie

```bash
python3 techniczne/kontakty/generate_vcards.py
```

## Testy podstawowe

```bash
python3 techniczne/kontakty/test_vcards.py . techniczne/kontakty/kontakty.yml
```

Test sprawdza m.in. UTF-8, CRLF, zawijanie do 75 oktetów, liczbę kontaktów, obowiązkowe pola oraz zgodność nazw i odnośników na stronie z jednym źródłem danych.

## Testy niezależnymi parserami

```bash
python3 -m pip install -r techniczne/kontakty/requirements-test.txt
python3 techniczne/kontakty/test_vcards_external.py .
```

Testy wykonują walidowany odczyt i ponowny odczyt po serializacji w bibliotekach `vobject` oraz `vobjectx`.

## Ograniczenie testów automatycznych

Automatyczne testy potwierdzają poprawność plików i danych, ale nie zastępują zachowania systemowego importera telefonu. Przed wdrożeniem docelowym ręcznie sprawdzono na rzeczywistym iPhonie wszystkie osiem plików pojedynczych oraz końcową nazwę wzorcowego kontaktu. Po każdej zmianie struktury vCard trzeba ponowić przynajmniej reprezentatywny test na urządzeniu.
