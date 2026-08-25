# Kontakty vCard

Ten katalog zawiera jedno źródło danych, generator i testy wizytówek używanych w przewodniku.

## Przyjęty model

- Format: vCard 3.0, UTF-8, zakończenia CRLF.
- Maksymalna długość fizycznego wiersza: 75 oktetów.
- `N:;;;;` pozostaje puste, ponieważ są to instytucje, a nie osoby. Zapobiega to zapisaniu całej nazwy jako imienia.
- `FN` zawiera krótką polską nazwę użytkową zaczynającą się od `Djerba —`.
- `ORG` zawiera nazwę właściwej instytucji.
- Krótkie numery alarmowe używają prostego `TEL`, bez technicznej etykiety `VOICE`.
- `EMAIL;TYPE=INTERNET` i `ADR;TYPE=WORK` występują tylko tam, gdzie mają praktyczne zastosowanie. Pole `EMAIL` nie używa niestandardowej dla vCard 3.0 etykiety `WORK`.
- `NOTE` wyjaśnia zastosowanie numeru; przecinki i średniki są escapowane.
- `CATEGORIES` zostało pominięte, ponieważ importery nie tworzą z niego niezawodnie listy kontaktów. Wspólne wyszukiwanie zapewnia prefiks `Djerba —`.

Paczka zbiorcza jest dokładnym połączeniem ośmiu plików pojedynczych. Utrzymywane są oba warianty, ponieważ poprawność wielokontaktowego VCF nie gwarantuje, że każda przeglądarka przekaże go bezpośrednio do systemowego importera.

## Generowanie

```bash
python3 techniczne/kontakty/generate_vcards.py
```

## Testy podstawowe

```bash
python3 techniczne/kontakty/test_vcards.py . techniczne/kontakty/kontakty.yml
```

Test sprawdza m.in. UTF-8, CRLF, zawijanie do 75 oktetów, liczbę i kolejność kontaktów, obowiązkowe pola oraz identyczność paczki z plikami pojedynczymi.

## Testy niezależnymi parserami

```bash
python3 -m pip install -r techniczne/kontakty/requirements-test.txt
python3 techniczne/kontakty/test_vcards_external.py .
```

Testy wykonują walidowany odczyt i ponowny odczyt po serializacji w bibliotekach `vobject` oraz `vobjectx`.

## Ograniczenie testów automatycznych

Automatyczne testy potwierdzają poprawność plików i danych, ale nie mogą zagwarantować, że przeglądarka mobilna uruchomi systemowy importer kontaktów. Apple oficjalnie opisuje na iPhonie import załącznika `.vcf` z wiadomości e-mail lub wiadomości. Dlatego po opublikowaniu izolowanej strony testowej pozostaje jeden krótki test na rzeczywistym iPhonie: paczka zbiorcza i jeden kontakt pojedynczy.
