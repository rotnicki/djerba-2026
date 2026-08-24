# Punkty 2 i 3 na mapie Dżerby

Status: korekta przygotowana 24 sierpnia 2026 r. po ponownej weryfikacji położenia.

## Zweryfikowane dane

Źródłem pozostaje zamrożony snapshot `tunisia-260822.osm.pbf` o SHA-256:

`4629c6f40e1749f266fa339ba484f473414cbb026c7b6267a47f16715266bfaf`

| Punkt | Miejsce | Obiekt OSM | Długość geograficzna | Szerokość geograficzna |
| --- | --- | --- | ---: | ---: |
| 2 | Erriadh i Djerbahood | węzeł `297765267` | `10.8543339°E` | `33.8190783°N` |
| 3 | synagoga El Ghriba | węzeł `297765095` | `10.8593929°E` | `33.8139230°N` |

Odległość geodezyjna na elipsoidzie WGS84 wynosi `739,2 m`. Punkt 3 leży na południowy wschód od punktu 2; azymut początkowy wynosi około `140,7°`.

## Przyczyna wcześniejszej niejednoznaczności

Rzeczywiste środki punktów dzieli na mapie około `11,9` jednostki SVG, a promień każdego numerowanego koła wynosi `15` jednostek. Koła narysowane dokładnie na współrzędnych nakładałyby się.

Wcześniejsza korekta przesuwała każde koło o około `24,8` jednostki. Odległość między pokazanymi środkami wzrosła przez to do około `61,4` jednostki, co wizualnie odpowiadało w przybliżeniu `3,8 km`. Dwa łączniki i dwie kropki wskazujące dokładne pozycje mogły wyglądać jak jedna przerywana linia między punktami.

## Przyjęta korekta

Koła są teraz odsuwane od siebie wzdłuż ich rzeczywistego układu tylko o tyle, ile potrzeba do zachowania niewielkiej przerwy:

- punkt 2: przesunięcie `−7` poziomo i `−9` pionowo;
- punkt 3: przesunięcie `+7` poziomo i `+9` pionowo;
- odległość między środkami kół po korekcie: około `34,7` jednostki SVG;
- odstęp między obrysami kół: około `4,7` jednostki SVG.

Każde przesunięcie ma około `11,4` jednostki, czyli jest mniejsze niż promień koła. Rzeczywista współrzędna pozostaje zatem wewnątrz odpowiedniego znacznika. W tej sytuacji generator nie rysuje osobnego punktu źródłowego ani łącznika. Usuwa to wrażenie przerywanej trasy bez ukrywania rzeczywistej bliskości miejsc.

Krótki opis `desc` SVG podaje, że punkty 2 i 3 dzieli około `740 m` i że koła są minimalnie rozsunięte dla czytelności.
