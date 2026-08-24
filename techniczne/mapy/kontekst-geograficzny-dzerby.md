# Kontekst geograficzny mapy Dżerby

Status: wdrożenie przygotowane 24 sierpnia 2026 r.

Ten dokument uzupełnia główną specyfikację `mapa-dzerby.md` o zmianę kadru i zawartości mapy wykonaną po ocenie użytkownika.

## Cel zmiany

Poprzedni kadr pokazywał Dżerbę niemal wyłącznie na tle wody. Utrudniało to rozpoznanie, że grafika jest wycinkiem większego obszaru i że wyspa ma stałe połączenie drogowe z Tunezją.

Aktualna mapa nadal służy do ogólnej orientacji, a nie do nawigacji. Dodaje tylko:

- minimalne fragmenty kontynentalnej Tunezji przy dolnej krawędzi;
- zamknięte wysepki widoczne na zachód i południowy zachód od Dżerby;
- pełne połączenie RR117 z podpisem `Grobla El Kantara – droga rzymska`;
- widoczny podpis `Kontynent – Tunezja`.

Nie dodano sieci dróg ani miejsc kontynentalnej Tunezji. Dalsze wyjazdy mają otrzymać osobną mapę szerszego obszaru.

## Dane i parametry

Mapa jest generowana z tego samego zamrożonego snapshotu `tunisia-260822.osm.pbf` o SHA-256:

`4629c6f40e1749f266fa339ba484f473414cbb026c7b6267a47f16715266bfaf`

Nowa ramka danych:

- zachód: `10.66°E`;
- wschód: `11.10°E`;
- południe: `33.59°N`;
- północ: `33.95°N`.

Generator domyka przecięte linie brzegowe do granic ramki i wybiera niewielkie wielokąty stałego lądu dotykające dolnej albo zachodniej krawędzi. Zamknięte wysepki są dołączane od powierzchni geometrii roboczej `0.00005°²`.

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

`6f521ae87524acb6b82e2990de526134bc709ce4ad580973420b5b1ba68c8aab`

Potwierdzono lokalnie:

- zgodność sumy snapshotu;
- identyczny wynik dwóch kolejnych uruchomień generatora;
- poprawność XML i unikatowość identyfikatorów;
- jedną warstwę lądu kontekstowego z sześcioma ścieżkami;
- po cztery ścieżki obrysu i środka grobli;
- obecność tytułu, opisu, `role="img"` i `aria-labelledby`;
- render w trybie jasnym i ciemnym;
- brak kolizji podpisu grobli z punktami, podziałką i znacznikiem północy.

Ręczny test VoiceOver pozostaje do wykonania po publikacji.
