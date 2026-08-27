# Kontekst geograficzny mapy Dżerby

Status: korekta styku kontynentu z krawędzią przygotowana 24 sierpnia 2026 r.; suma kontrolna i kontrola kolizji z lotniskiem zaktualizowane 27 sierpnia 2026 r.

Ten dokument uzupełnia główną specyfikację `mapa-dzerby.md` o zmianę kadru i zawartości mapy wykonaną po ocenie użytkownika.

## Cel zmiany

Poprzedni kadr pokazywał Dżerbę niemal wyłącznie na tle wody. Utrudniało to rozpoznanie, że grafika jest wycinkiem większego obszaru i że wyspa ma stałe połączenie drogowe z Tunezją.

Aktualna mapa nadal służy do ogólnej orientacji, a nie do nawigacji. Dodaje tylko:

- minimalne fragmenty kontynentalnej Tunezji przy dolnej krawędzi;
- zamknięte wysepki widoczne na zachód i południowy zachód od Dżerby;
- pełne połączenie RR117 z podpisem `Grobla El Kantara – droga rzymska`;
- widoczny podpis `Kontynent – Tunezja`.

Nie dodano sieci dróg ani miejsc kontynentalnej Tunezji. Dalsze wyjazdy mają otrzymać osobną mapę szerszego obszaru.

## Korekta po ocenie użytkownika

Pierwsza wersja kontekstu domykała kontynent na granicach ramki danych `10.66–11.10°E` i `33.59–33.95°N`. Sama ramka była jednak rysowana wewnątrz SVG z marginesami wynikającymi z proporcji mapy. W efekcie kontynent kończył się przed fizyczną krawędzią grafiki i wyglądał jak dwie dodatkowe wyspy.

Generator wyznacza teraz odwrotnym przeliczeniem współrzędne odpowiadające czterem rzeczywistym krawędziom płótna `960 × 760`. Kontury kontynentu są domykane dopiero do tych granic. Lewy fragment lądu dochodzi do lewej i dolnej krawędzi, a fragment połączony groblą dochodzi do dolnej krawędzi. Zamknięte pozostają wyłącznie prawdziwe wysepki.

Warstwa kontekstowego lądu jest przycinana zaokrągloną maską `djerba-map-clip`, aby ląd dochodzący do krawędzi nie naruszał narożników mapy.

## Dane i parametry

Mapa jest generowana z tego samego zamrożonego snapshotu `tunisia-260822.osm.pbf` o SHA-256:

`4629c6f40e1749f266fa339ba484f473414cbb026c7b6267a47f16715266bfaf`

Nowa ramka danych:

- zachód: `10.66°E`;
- wschód: `11.10°E`;
- południe: `33.59°N`;
- północ: `33.95°N`.

Generator zbiera linie brzegowe z technicznym zapasem `0.16°` długości i `0.08°` szerokości geograficznej. Następnie domyka je do granic odpowiadających fizycznym krawędziom SVG i wybiera wielokąty stałego lądu wychodzące poza kadr. Zapas służy tylko poprawnemu odtworzeniu konturów przy krawędzi; nie zmienia położenia Dżerby, punktów ani podziałki. Zamknięte wysepki są dołączane od powierzchni geometrii roboczej `0.00005°²`.

Grobla jest odtwarzana z czterech zapisanych odcinków OSM:

- `31360290`;
- `198577347`;
- `198577348`;
- `31360293`.

Brak któregokolwiek z nich przerywa generowanie zamiast tworzyć niepełne połączenie.

## Wygląd i dostępność

Kontekstowy ląd ma osobny token `--map-context-land`:

- tryb jasny: `#e8dfc2`;
- tryb ciemny: `#252a22`;
- wymuszone kolory: `Canvas`.

Grobla jest linią dwuwarstwową: obrys ma szerokość `7`, a środek `3` jednostki SVG. Odróżnia się więc od zwykłych dróg nie tylko kolorem. Kontynent ma widoczny podpis tekstowy.

Dwuwarstwowy zapis przedstawia jedną drogę RR117, a nie dwa równoległe połączenia. Po ocenie użytkownika do podpisu `Grobla El Kantara – droga rzymska` dodano linię prowadzącą. Łączy ona lewą krawędź podpisu z punktem `10.926282°E, 33.656141°N`, położonym bezpośrednio na zapisanym odcinku grobli. Dzięki temu podpis nie może być odczytany jako nazwa sąsiednich wysepek.

Krótki opis `desc` SVG wymienia Dżerbę, pobliskie wysepki, fragment kontynentu i Groblę El Kantara. Wewnętrzna geometria pozostaje ukryta przed czytnikiem ekranu, a całe SVG zachowuje model jednej grafiki z `role="img"`.

Kontrast nowych par:

| Para | Jasny | Ciemny |
| --- | ---: | ---: |
| etykieta / ląd kontekstowy | 11,81:1 | 13,97:1 |
| obrys / ląd kontekstowy | 5,51:1 | 8,32:1 |

## Odtworzenie i kontrola

Polecenie z katalogu głównego repozytorium:

```bash
python techniczne/mapy/generate_djerba_map.py \
  /tmp/tunisia-260822.osm.pbf \
  _includes/maps/djerba.svg
```

SHA-256 wynikowego SVG:

`3d296d81fd81a709caac1673d8b369c056d2e63e261edf2a2f8cd7d70602f3ef`

Potwierdzono lokalnie:

- zgodność sumy snapshotu;
- identyczny wynik dwóch kolejnych uruchomień generatora;
- poprawność XML i unikatowość identyfikatorów;
- jedną warstwę lądu kontekstowego z sześcioma ścieżkami;
- dojście obu fragmentów kontynentu do fizycznej krawędzi SVG;
- pozostawienie prawdziwych wysepek jako zamkniętych kształtów;
- działanie zaokrąglonej maski przy narożnikach;
- po cztery ścieżki obrysu i środka grobli;
- obecność tytułu, opisu, `role="img"` i `aria-labelledby`;
- render w trybie jasnym i ciemnym;
- brak kolizji podpisu grobli z punktami, podziałką i znacznikiem północy.
- jednoznaczne połączenie podpisu linią prowadzącą z właściwą ścieżką RR117.
- brak kolizji kwadratowego znacznika L i podpisu lotniska z Houmt Souk, Erriadh i linią brzegową.

Ręczny test VoiceOver pozostaje do wykonania po publikacji.
