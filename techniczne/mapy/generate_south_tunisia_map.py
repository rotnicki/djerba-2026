#!/usr/bin/env python3
"""Generate the broad Djerba and south Tunisia SVG map.

Usage:
    python techniczne/mapy/generate_south_tunisia_map.py \
        ../tunisia-260822.osm.pbf _includes/maps/south-tunisia.svg

The map is deliberately orientational. It uses the frozen OSM snapshot for
coastlines, selected main roads, Chott el-Jerid and every marked place, but it
does not claim to show an excursion route or provide navigation.
"""

from __future__ import annotations

import argparse
import html
import math
from pathlib import Path

import osmium
from shapely import wkb
from shapely.geometry import LineString, Point, Polygon, box
from shapely.ops import linemerge, polygonize, unary_union


SNAPSHOT_SHA256 = "4629c6f40e1749f266fa339ba484f473414cbb026c7b6267a47f16715266bfaf"

WEST, SOUTH, EAST, NORTH = 7.80, 32.70, 11.15, 34.42
VIEW_WIDTH, VIEW_HEIGHT = 1000, 660
PAD_X, PAD_Y = 46, 44
MARKER_RADIUS = 13
MARKER_GAP = 4
KM_PER_DEGREE_LATITUDE = 111.32
SCALE_DISTANCE_KM = 100
# The geographic content has extra canvas padding after projection. Keep a
# wider extraction margin so the mainland coastline reaches the canvas edges
# and can divide land from the Gulf of Gabes without an artificial gap.
DATA_MARGIN_LON = 0.30
DATA_MARGIN_LAT = 0.30

CHOTT_EL_JERID_RELATION = 3969167
KSAR_OULED_SOLTANE_RELATION = 2516832

POIS = (
    {
        "number": "H",
        "kind": "hotel",
        "name": "Club Palm Azur",
        "node": 1123865146,
        "label_dx": -20,
        "label_dy": -16,
        "anchor": "end",
    },
    {
        "number": "1",
        "kind": "place",
        "name": "Grobla El Kantara",
        "node": 6616525005,
        "label_dx": -20,
        "label_dy": 26,
        "anchor": "end",
    },
    {
        "number": "2",
        "kind": "place",
        "name": "Medenine",
        "node": 287585326,
        "label_dx": 20,
        "label_dy": -16,
        "anchor": "start",
    },
    {
        "number": "3",
        "kind": "place",
        "name": "Tataouine",
        "node": 264885332,
        "label_dx": 20,
        "label_dy": 24,
        "anchor": "start",
    },
    {
        "number": "4",
        "kind": "place",
        "name": "Chenini",
        "node": 297760994,
        "label_dx": -20,
        "label_dy": 24,
        "anchor": "end",
    },
    {
        "number": "5",
        "kind": "place",
        "name": "Ksar Hadada",
        "way": 215111919,
        "label_dx": -20,
        "label_dy": -18,
        "anchor": "end",
    },
    {
        "number": "6",
        "kind": "place",
        "name": "Ksar Ouled Soltane",
        "relation": KSAR_OULED_SOLTANE_RELATION,
        "label_dx": 20,
        "label_dy": 24,
        "anchor": "start",
    },
    {
        "number": "7",
        "kind": "place",
        "name": "Toujane",
        "node": 1997328129,
        "label_dx": -20,
        "label_dy": 32,
        "anchor": "end",
    },
    {
        "number": "8",
        "kind": "place",
        "name": "Matmata i Hotel Sidi Idriss",
        "node": 559400323,
        "label_dx": -20,
        "label_dy": -24,
        "anchor": "end",
    },
    {
        "number": "9",
        "kind": "place",
        "name": "Ksar Ghilane",
        "node": 264887592,
        "label_dx": -20,
        "label_dy": 24,
        "anchor": "end",
    },
    {
        "number": "10",
        "kind": "place",
        "name": "Douz i Zaafrane",
        "node": 264881676,
        "label_dx": -20,
        "label_dy": 24,
        "anchor": "end",
    },
    {
        "number": "11",
        "kind": "place",
        "name": "Tozeur",
        "node": 298018887,
        "label_dx": 20,
        "label_dy": 24,
        "anchor": "start",
    },
    {
        "number": "12",
        "kind": "place",
        "name": "Chebika",
        "node": 6853346685,
        "label_dx": 20,
        "label_dy": -18,
        "anchor": "start",
    },
)


def overlaps_bbox(coords: list[tuple[float, float]]) -> bool:
    if not coords:
        return False
    xs = [coord[0] for coord in coords]
    ys = [coord[1] for coord in coords]
    return (
        max(xs) >= WEST - DATA_MARGIN_LON
        and min(xs) <= EAST + DATA_MARGIN_LON
        and max(ys) >= SOUTH - DATA_MARGIN_LAT
        and min(ys) <= NORTH + DATA_MARGIN_LAT
    )


class SouthTunisiaData(osmium.SimpleHandler):
    def __init__(self) -> None:
        super().__init__()
        self.coastlines: list[LineString] = []
        self.roads: list[LineString] = []
        self.poi_nodes: dict[int, tuple[float, float]] = {}
        self.poi_ways: dict[int, tuple[float, float]] = {}
        self._poi_node_ids = {item["node"] for item in POIS if "node" in item}
        self._poi_way_ids = {item["way"] for item in POIS if "way" in item}

    def node(self, node: osmium.osm.Node) -> None:
        if node.id in self._poi_node_ids:
            self.poi_nodes[node.id] = (node.location.lon, node.location.lat)

    def way(self, way: osmium.osm.Way) -> None:
        is_coastline = way.tags.get("natural") == "coastline"
        is_main_road = way.tags.get("highway") in {"trunk", "primary", "secondary"}
        is_poi = way.id in self._poi_way_ids
        if not (is_coastline or is_main_road or is_poi):
            return

        try:
            coords = [(node.lon, node.lat) for node in way.nodes]
        except osmium.InvalidLocationError:
            return
        if not coords:
            return

        if is_poi:
            polygon = Polygon(coords) if len(coords) >= 4 and coords[0] == coords[-1] else None
            geometry = polygon if polygon and polygon.is_valid else LineString(coords)
            center = geometry.centroid
            self.poi_ways[way.id] = (center.x, center.y)

        if not overlaps_bbox(coords) or len(coords) < 2:
            return
        if is_coastline:
            self.coastlines.append(LineString(coords))
        if is_main_road:
            self.roads.append(LineString(coords))


def load_relation_geometries(pbf: Path) -> dict[int, object]:
    relation_ids = {CHOTT_EL_JERID_RELATION, KSAR_OULED_SOLTANE_RELATION}
    factory = osmium.geom.WKBFactory()
    processor = (
        osmium.FileProcessor(str(pbf))
        .with_areas(osmium.filter.IdFilter(relation_ids))
        .with_filter(osmium.filter.EntityFilter(osmium.osm.AREA))
    )
    geometries: dict[int, object] = {}
    for area in processor:
        relation_id = area.orig_id()
        if relation_id in relation_ids:
            geometries[relation_id] = wkb.loads(
                factory.create_multipolygon(area), hex=True
            )
    missing = relation_ids - geometries.keys()
    if missing:
        raise RuntimeError(
            "Missing configured OSM relations: "
            + ", ".join(str(value) for value in sorted(missing))
        )
    return geometries


def projection():
    latitude_scale = math.cos(math.radians((SOUTH + NORTH) / 2))
    projected_width = (EAST - WEST) * latitude_scale
    projected_height = NORTH - SOUTH
    scale = min(
        (VIEW_WIDTH - 2 * PAD_X) / projected_width,
        (VIEW_HEIGHT - 2 * PAD_Y) / projected_height,
    )
    content_width = projected_width * scale
    content_height = projected_height * scale
    offset_x = (VIEW_WIDTH - content_width) / 2
    offset_y = (VIEW_HEIGHT - content_height) / 2

    def project(lon: float, lat: float) -> tuple[float, float]:
        x = offset_x + (lon - WEST) * latitude_scale * scale
        y = offset_y + (NORTH - lat) * scale
        return x, y

    canvas_west = WEST - offset_x / (latitude_scale * scale)
    canvas_east = WEST + (VIEW_WIDTH - offset_x) / (latitude_scale * scale)
    canvas_north = NORTH + offset_y / scale
    canvas_south = NORTH - (VIEW_HEIGHT - offset_y) / scale
    return project, scale, box(canvas_west, canvas_south, canvas_east, canvas_north)


def path_data(coords, project, close: bool = False) -> str:
    points = [project(lon, lat) for lon, lat in coords]
    if not points:
        return ""
    parts = [f"M {points[0][0]:.1f} {points[0][1]:.1f}"]
    parts.extend(f"L {x:.1f} {y:.1f}" for x, y in points[1:])
    if close:
        parts.append("Z")
    return " ".join(parts)


def geometry_paths(geometry, project, simplify: float) -> list[str]:
    simplified = geometry.simplify(simplify, preserve_topology=True)
    polygons = [simplified] if simplified.geom_type == "Polygon" else list(simplified.geoms)
    paths = []
    for polygon in polygons:
        parts = [path_data(polygon.exterior.coords, project, close=True)]
        parts.extend(path_data(ring.coords, project, close=True) for ring in polygon.interiors)
        paths.append(" ".join(part for part in parts if part))
    return paths


def reconstruct_land(coastlines: list[LineString], viewport: Polygon):
    clipped = [line.intersection(viewport) for line in coastlines if line.intersects(viewport)]
    pieces = list(polygonize(unary_union([*clipped, viewport.boundary])))
    mainland_anchor = Point(9.5, 33.5)
    mainland_candidates = [polygon for polygon in pieces if polygon.covers(mainland_anchor)]
    if not mainland_candidates:
        raise RuntimeError("Could not reconstruct the continental coastline")
    mainland = max(mainland_candidates, key=lambda polygon: polygon.area)

    closed = list(polygonize(unary_union(coastlines)))
    islands = [
        polygon
        for polygon in closed
        if polygon.area >= 0.00015
        and polygon.intersects(viewport)
        and not mainland.covers(polygon.representative_point())
    ]
    if not any(polygon.covers(Point(10.91, 33.80)) for polygon in islands):
        raise RuntimeError("Could not reconstruct Djerba in the broad map")
    return mainland, islands


def make_svg(
    data: SouthTunisiaData, relation_geometries: dict[int, object]
) -> str:
    project, projection_scale, viewport = projection()
    mainland, islands = reconstruct_land(data.coastlines, viewport)
    land_geometries = [mainland, *islands]
    land_union = unary_union(land_geometries)
    land_paths = []
    for geometry in land_geometries:
        land_paths.extend(geometry_paths(geometry, project, 0.0012))

    merged_roads = linemerge(unary_union(data.roads))
    road_parts = [merged_roads] if merged_roads.geom_type == "LineString" else list(merged_roads.geoms)
    road_paths = []
    for road in road_parts:
        clipped = road.intersection(land_union)
        parts = [clipped] if clipped.geom_type == "LineString" else list(getattr(clipped, "geoms", []))
        for part in parts:
            simplified = part.simplify(0.0012, preserve_topology=True)
            if simplified.length >= 0.012:
                road_paths.append(path_data(simplified.coords, project))

    chott = relation_geometries[CHOTT_EL_JERID_RELATION].intersection(viewport)
    chott_paths = geometry_paths(chott, project, 0.003)

    relation_centers = {
        KSAR_OULED_SOLTANE_RELATION: relation_geometries[
            KSAR_OULED_SOLTANE_RELATION
        ].centroid.coords[0]
    }
    missing = []
    for item in POIS:
        if "node" in item and item["node"] not in data.poi_nodes:
            missing.append(str(item["node"]))
        if "way" in item and item["way"] not in data.poi_ways:
            missing.append(str(item["way"]))
        if "relation" in item and item["relation"] not in relation_centers:
            missing.append(str(item["relation"]))
    if missing:
        raise RuntimeError("Missing configured OSM objects: " + ", ".join(missing))

    poi_layout = []
    for item in POIS:
        if "node" in item:
            lon, lat = data.poi_nodes[item["node"]]
        elif "way" in item:
            lon, lat = data.poi_ways[item["way"]]
        else:
            lon, lat = relation_centers[item["relation"]]
        origin_x, origin_y = project(lon, lat)
        marker_x = origin_x + item.get("marker_dx", 0)
        marker_y = origin_y + item.get("marker_dy", 0)
        poi_layout.append(
            {
                "item": item,
                "origin_x": origin_x,
                "origin_y": origin_y,
                "marker_x": marker_x,
                "marker_y": marker_y,
                "label_x": marker_x + item["label_dx"],
                "label_y": marker_y + item["label_dy"],
            }
        )

    minimum_marker_distance = 2 * MARKER_RADIUS + MARKER_GAP
    for index, first in enumerate(poi_layout):
        for second in poi_layout[index + 1 :]:
            distance = math.hypot(
                first["marker_x"] - second["marker_x"],
                first["marker_y"] - second["marker_y"],
            )
            if distance < minimum_marker_distance:
                raise RuntimeError(
                    "Configured map markers overlap: "
                    f'{first["item"]["number"]} and {second["item"]["number"]} '
                    f"are {distance:.1f} SVG units apart"
                )

    scale_width = projection_scale * SCALE_DISTANCE_KM / KM_PER_DEGREE_LATITUDE
    scale_start_x = 66
    scale_end_x = scale_start_x + scale_width
    scale_middle_x = (scale_start_x + scale_end_x) / 2
    scale_y = 600
    djerba_x, djerba_y = project(10.86, 33.89)
    chott_x, chott_y = project(8.39, 33.73)

    lines = [
        '<svg class="place-map__graphic place-map__graphic--regional" viewBox="0 0 1000 660" role="img"',
        '  aria-labelledby="south-tunisia-map-title south-tunisia-map-desc" xmlns="http://www.w3.org/2000/svg">',
        '  <title id="south-tunisia-map-title">Dżerba i południe Tunezji: orientacyjna mapa wycieczek</title>',
        '  <desc id="south-tunisia-map-desc">Mapa pokazuje położenie hotelu Club Palm Azur na Dżerbie oraz dwanaście miejsc i kierunków wycieczek na kontynencie. Litera H oznacza hotel. Numery od 1 do 12 wskazują Groblę El Kantara, Medenine, Tataouine, Chenini, Ksar Hadada, Ksar Ouled Soltane, Toujane, Matmatę z Hotelem Sidi Idriss, Ksar Ghilane, Douz z Zaafrane, Tozeur i Chebikę. Chott el-Jerid pokazano jako rozległy obszar. W lewym dolnym rogu znajduje się podziałka od 0 do 100 kilometrów. Szczegółowy opis relacji przestrzennych znajduje się pod mapą.</desc>',
        f'  <metadata>OpenStreetMap snapshot tunisia-260822.osm.pbf, SHA-256 {SNAPSHOT_SHA256}</metadata>',
        '  <defs aria-hidden="true">',
        '    <clipPath id="south-tunisia-map-clip">',
        '      <rect width="1000" height="660" rx="12"/>',
        '    </clipPath>',
        '  </defs>',
        '  <rect class="place-map__water" width="1000" height="660" rx="12"/>',
        '  <g class="place-map__land" clip-path="url(#south-tunisia-map-clip)" aria-hidden="true">',
    ]
    lines.extend(f'    <path fill-rule="evenodd" d="{value}"/>' for value in land_paths if value)
    lines.extend([
        '  </g>',
        '  <g class="place-map__salt-lake" aria-hidden="true">',
    ])
    lines.extend(f'    <path fill-rule="evenodd" d="{value}"/>' for value in chott_paths if value)
    lines.extend([
        '  </g>',
        '  <g class="place-map__roads place-map__roads--regional" aria-hidden="true">',
    ])
    lines.extend(f'    <path d="{value}"/>' for value in road_paths if value)
    lines.extend([
        '  </g>',
        '  <g class="place-map__context" aria-hidden="true">',
        f'    <text class="place-map__geography-label" x="{djerba_x:.1f}" y="{djerba_y:.1f}" text-anchor="middle">Dżerba</text>',
        f'    <text class="place-map__area-label" x="{chott_x:.1f}" y="{chott_y:.1f}" text-anchor="middle">Chott el-Jerid</text>',
        '  </g>',
        '  <g class="place-map__points" aria-hidden="true">',
        '    <g class="place-map__leaders">',
    ])

    for point in poi_layout:
        item = point["item"]
        x, y = point["marker_x"], point["marker_y"]
        lx, ly = point["label_x"], point["label_y"]
        line_end_x = lx - 8 if item["anchor"] == "start" else lx + 8
        lines.append(
            f'      <path class="place-map__leader" d="M {x:.1f} {y:.1f} L {line_end_x:.1f} {ly - 5:.1f}"/>'
        )

    lines.extend([
        '    </g>',
        '    <g class="place-map__labels">',
    ])
    for point in poi_layout:
        item = point["item"]
        lines.append(
            f'      <text class="place-map__point-label" x="{point["label_x"]:.1f}" y="{point["label_y"]:.1f}" text-anchor="{item["anchor"]}">{html.escape(item["name"])}</text>'
        )

    lines.extend([
        '    </g>',
        '    <g class="place-map__markers">',
    ])
    for point in poi_layout:
        item = point["item"]
        x, y = point["marker_x"], point["marker_y"]
        marker_class = "place-map__marker place-map__marker--hotel" if item["kind"] == "hotel" else "place-map__marker"
        lines.append(f'      <g class="{marker_class}">')
        if item["kind"] == "hotel":
            size = MARKER_RADIUS
            points = f"{x:.1f},{y-size:.1f} {x+size:.1f},{y:.1f} {x:.1f},{y+size:.1f} {x-size:.1f},{y:.1f}"
            lines.append(f'        <polygon points="{points}"/>')
        else:
            lines.append(f'        <circle cx="{x:.1f}" cy="{y:.1f}" r="{MARKER_RADIUS}"/>')
        lines.append(
            f'        <text class="place-map__marker-text" x="{x:.1f}" y="{y + 5.5:.1f}" text-anchor="middle">{item["number"]}</text>'
        )
        lines.append('      </g>')

    lines.extend([
        '    </g>',
        '  </g>',
        '  <g class="place-map__scale" aria-hidden="true">',
        f'    <text x="{scale_middle_x:.1f}" y="576" text-anchor="middle">Skala</text>',
        f'    <path d="M {scale_start_x:.1f} {scale_y:.1f} H {scale_end_x:.1f} M {scale_start_x:.1f} {scale_y - 10:.1f} V {scale_y + 10:.1f} M {scale_middle_x:.1f} {scale_y - 7:.1f} V {scale_y + 7:.1f} M {scale_end_x:.1f} {scale_y - 10:.1f} V {scale_y + 10:.1f}"/>',
        f'    <text x="{scale_start_x:.1f}" y="628" text-anchor="middle">0</text>',
        f'    <text x="{scale_middle_x:.1f}" y="628" text-anchor="middle">50</text>',
        f'    <text x="{scale_end_x:.1f}" y="628" text-anchor="middle">100 km</text>',
        '  </g>',
        '  <g class="place-map__north" aria-hidden="true" transform="translate(944 70)">',
        '    <path d="M 0 28 L 0 -16 M -7 -5 L 0 -16 L 7 -5"/>',
        '    <text x="0" y="46" text-anchor="middle">N</text>',
        '  </g>',
        '</svg>',
        '',
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pbf", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    data = SouthTunisiaData()
    data.apply_file(str(args.pbf), locations=True)
    relation_geometries = load_relation_geometries(args.pbf)
    output = make_svg(data, relation_geometries)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
