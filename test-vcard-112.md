# Test vCard 112

Wszystkie trzy pliki zawierają ten sam numer telefonu `112` i tę samą wartość pola `FN`: `Polski numer alarmowy`. Nie zawierają pola `N`. Różnią się wyłącznie polem `ORG`.

## Test A — bez organizacji

`FN:Polski numer alarmowy`

Brak pola `ORG`.

[Test A — otwórz kontakt 112 bez organizacji](assets/kontakty/test-112-a-bez-organizacji.vcf)

## Test B — organizacja identyczna z FN

`FN:Polski numer alarmowy`

`ORG:Polski numer alarmowy`

[Test B — otwórz kontakt 112 z identyczną organizacją](assets/kontakty/test-112-b-organizacja-identyczna.vcf)

## Test C — organizacja celowo inna

`FN:Polski numer alarmowy`

`ORG:Przykładowa organizacja testowa`

[Test C — otwórz kontakt 112 z inną organizacją](assets/kontakty/test-112-c-organizacja-inna.vcf)
