# Wizualizacje — stan i plan rozwoju

Ten dokument zapisuje ustalenia dotyczące materiałów wizualnych w publicznym przewodniku. Ma utrwalać zarówno rozwiązania już wdrożone, jak i pomysły przeznaczone do dalszych testów.

## Zasada podstawowa

W przewodniku nie wykorzystujemy obrazów generowanych przez AI. Korzystamy z istniejących materiałów mających wiarygodne źródło i jasne warunki wykorzystania oraz z map renderowanych z rzeczywistych danych kartograficznych.

Tekst pozostaje podstawowym źródłem informacji. Obraz ma uzupełniać treść, a nie zastępować opis potrzebny osobie korzystającej z czytnika ekranu.

## Stan obecny — strona główna

Na stronie głównej `index.md` działa obecnie testowe wdrożenie obrazu otwierającego przewodnik.

Wykorzystany materiał:

- plik: `Djerba Island.jpeg`;
- charakter: zdjęcie satelitarne Dżerby z Landsat 8;
- data zobrazowania: 4 maja 2020 r.;
- źródło publikacyjne: NASA Earth Observatory / Lauren Dauphin, dane USGS;
- miejsce pozyskania do strony: Wikimedia Commons;
- status prawny podany przy pliku: domena publiczna.

Kopia obrazu używana na stronie jest przechowywana lokalnie w repozytorium jako `assets/images/djerba-island-landsat-2020.jpg` i osadzona w sekcji `home-hero`. Wikimedia Commons pozostaje wskazane jako miejsce pozyskania i źródło informacji o pochodzeniu. Obraz ma rozbudowany tekst alternatywny opisujący kształt wyspy i najważniejsze elementy orientacyjne, podpis oraz osobną informację o autorstwie i źródle na dole strony.

To wdrożenie traktujemy jako pierwszy wzorzec do oceny: sprawdzamy jednocześnie wygląd, użyteczność, sposób opisu alternatywnego, prezentację źródła i zachowanie strony na urządzeniach mobilnych oraz z technologiami asystującymi. Nie oznacza ono jeszcze automatycznego zastosowania identycznego układu do wszystkich dalszych materiałów.

## Zdjęcia reprezentujące miejsca w przewodniku po wycieczkach

Planowany jest rozwój `wycieczki.md` o istniejące zdjęcia reprezentujące opisywane miejsca. Celem nie jest galeria zdjęć, lecz ułatwienie szybkiej orientacji osobom widzącym i słabowidzącym oraz pokazanie charakterystycznego wyglądu danego miejsca.

Robocza lista miejsc do objęcia tym rozwiązaniem:

1. Dżerba;
2. Houmt Souk i Borj Ghazi Mustapha;
3. Erriadh i Djerbahood;
4. El Ghriba;
5. Guellala;
6. Djerba Explore;
7. Ras Rmel;
8. El Kantara;
9. Medenine;
10. Tataouine;
11. Chenini;
12. Ksar Hadada;
13. Ksar Ouled Soltane;
14. Toujane;
15. Matmata;
16. Hotel Sidi Idriss;
17. Ksar Ghilane;
18. Douz;
19. Chott el-Jerid;
20. Tozeur i górskie oazy.

Domyślnie szukamy jednego dobrze dobranego, reprezentatywnego zdjęcia dla miejsca. Dwa zdjęcia można rozważyć tylko wtedy, gdy jedna pozycja rzeczywiście obejmuje dwa istotnie różne obiekty lub krajobrazy, np. Houmt Souk i fort albo Tozeur i górskie oazy.

## Zasady doboru zdjęć

Przed wprowadzeniem zdjęcia do strony należy sprawdzić:

- czy przedstawia dokładnie opisywane miejsce, a nie tylko podobny obiekt lub ogólny krajobraz regionu;
- czy jest reprezentatywne i pomaga zrozumieć charakter miejsca;
- źródło, autora, licencję lub status domeny publicznej;
- czy warunki licencji pozwalają na publikację na GitHub Pages;
- jakość i rozdzielczość wystarczającą dla strony;
- czy możliwe jest przygotowanie rzeczowego tekstu alternatywnego bez zgadywania elementów zdjęcia.

Preferowanym źródłem dla tego etapu jest Wikimedia Commons, szczególnie gdy dostępne są dobrze opisane fotografie z jasną licencją. Inne źródła mogą być użyte tylko po osobnym sprawdzeniu praw do wykorzystania.

Nie wybieramy zdjęcia wyłącznie dlatego, że jest efektowne. Ważniejsza jest zgodność z miejscem i użyteczność informacyjna.

## Sposób wdrażania

Nie wprowadzamy od razu wszystkich zdjęć według nieprzetestowanego wzorca.

Przyjmujemy kolejność:

1. wybór jednego miejsca;
2. znalezienie i zweryfikowanie jednego zdjęcia;
3. przygotowanie tekstu alternatywnego, podpisu i informacji o źródle;
4. osadzenie go w jednym miejscu strony;
5. sprawdzenie całej ścieżki użytkownika, w tym na urządzeniu mobilnym i z czytnikiem ekranu;
6. dopiero po zaakceptowaniu wzorca zastosowanie go do kolejnych miejsc.

Nie dokładamy dodatkowych galerii, karuzel, skryptów ani innych mechanizmów, jeśli nie okażą się potrzebne.

## Zdjęcia a mapy

Zdjęcia i mapy pełnią różne funkcje i nie zastępują się wzajemnie:

- zdjęcie odpowiada przede wszystkim na pytanie: „jak wygląda to miejsce?”;
- mapa odpowiada przede wszystkim na pytanie: „gdzie to miejsce leży i jak ma się do innych punktów lub trasy?”.

Plan własnych uproszczonych map opartych na danych OpenStreetMap jest dokumentowany osobno w `techniczne/mapy/README.md`.

Docelowo przy wycieczkach mogą więc występować oba rodzaje materiałów, ale każdy tylko wtedy, gdy rzeczywiście pomaga w zrozumieniu treści.

## Status

- zdjęcie satelitarne na stronie głównej — wdrożone testowo;
- zdjęcia reprezentujące poszczególne miejsca w `wycieczki.md` — planowane, wybór zdjęć jeszcze nie został wykonany dla całej listy;
- własne uproszczone mapy OpenStreetMap — planowane; przygotowano zasady archiwizacji danych źródłowych, ale właściwy snapshot i mapy nie zostały jeszcze wykonane.
