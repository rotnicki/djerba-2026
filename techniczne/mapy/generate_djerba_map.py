#!/usr/bin/env python3
"""Generate the simplified Djerba SVG map from the frozen Tunisia OSM PBF.

Usage:
    python techniczne/mapy/generate_djerba_map.py \
        ../tunisia-260822.osm.pbf _includes/maps/djerba.svg

The script intentionally keeps the island dominant while adding only enough
nearby coastline, islets and the El Kantara causeway to explain its geographic
context.  It also includes selected main roads and the places described in the
guide.  It requires pyosmium and Shapely.

Implementation records: techniczne/mapy/mapa-dzerby.md and
techniczne/mapy/kontekst-geograficzny-dzerby.md and
techniczne/mapy/punkty-2-i-3.md
"""

from __future__ import annotations

import argparse
import html
import math
from pathlib import Path

import osmium
from shapely.geometry import LineString, Point, Polygon, box
from shapely.ops import polygonize, unary_union


SNAPSHOT_SHA256 = "4629c6f40e1749f266fa339ba484f473414cbb026c7b6267a47f16715266bfaf"

# The context remains deliberately tight: Djerba is dominant, but the western
# islets, both nearby pieces of mainland and the complete Roman causeway fit in
# the frame.  A separate map will cover excursions farther into Tunisia.
WEST, SOUTH, EAST, NORTH = 10.66, 33.59, 11.10, 33.95
VIEW_WIDTH, VIEW_HEIGHT = 960, 760
PAD_X, PAD_Y = 54, 58
MARKER_RADIUS = 15
MARKER_GAP = 4
KM_PER_DEGREE_LATITUDE = 111.32
SCALE_DISTANCE_KM = 10
MIN_CONTEXT_ISLAND_AREA = 0.00005
DATA_MARGIN_LON = 0.16
DATA_MARGIN_LAT = 0.08
CAUSEWAY_LABEL_TARGET = (10.926282, 33.656141)

# Core RR117 segments forming the El Kantara connection from Djerba to the
# mainland in the frozen 2026-08-22 snapshot.
CAUSEWAY_WAY_IDS = {
    31360290,
    198577347,
    198577348,
    31360293,
}


POIS = (
    {
        "number": "H",
        "kind": "hotel",
        "name": "Hotel Club Palm Azur",
        "node": 1123865146,
        "label_dx": 18,
        "label_dy": 28,
        "anchor": "start",
    },
    {
        "number": "1",
        "kind": "place",
        "name": "Houmt Souk i fort",
        "node": 9335010754,
        "label_dx": 18,
        "label_dy": -18,
        "anchor": "start",
    },
    {
        "number": "2",
        "kind": "place",
        "name": "Erriadh i Djerbahood",
        "node": 297765267,
        "marker_dx": -7,
        "marker_dy": -9,
        "label_dx": -20,
        "label_dy": -28,
        "anchor": "end",
    },
    {
        "number": "3",
        "kind": "place",
        "name": "Synagoga El Ghriba",
        "node": 297765095,
        "marker_dx": 7,
        "marker_dy": 9,
        "label_dx": 20,
        "label_dy": 32,
        "anchor": "start",
    },
    {
        "number": "4",
        "kind": "place",
        "name": "Guellala",
        "node": 1259516109,
        "label_dx": -18,
        "label_dy": 30,
        "anchor": "end",
    },
    {
        "number": "5",
        "kind": "place",
        "name": "Djerba Explore",
        "way": 213910588,
        "label_dx": -18,
        "label_dy": -18,
        "anchor": "end",
    },
    {
        "number": "6",
        "kind": "place",
        "name": "Ras Rmel",
        "node": 10820734092,
        "label_dx": 18,
        "label_dy": -12,
        "anchor": "start",
    },
)

CONTEXT_NODES = {
    287613682: "Midoun",
}


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


class DjerbaData(osmium.SimpleHandler):
    def __init__(self) -> None:
        super().__init__()
        self.coastlines: list[LineString] = []
        self.roads: list[LineString] = []
        self.causeway_roads: dict[int, LineString] = {}
        self.poi_nodes: dict[int, tuple[float, float]] = {}
        self.poi_ways: dict[int, tuple[float, float]] = {}
        self.context_nodes: dict[int, tuple[float, float]] = {}
        self._poi_node_ids = {item["node"] for item in POIS if "node" in item}
        self._poi_way_ids = {item["way"] for item in POIS if "way" in item}

    def node(self, node: osmium.osm.Node) -> None:
        if node.id in self._poi_node_ids:
            self.poi_nodes[node.id] = (node.location.lon, node.location.lat)
        if node.id in CONTEXT_NODES:
            self.context_nodes[node.id] = (node.location.lon, node.location.lat)

    def way(self, way: osmium.osm.Way) -> None:
        try:
            coords = [(node.lon, node.lat) for node in way.nodes]
        except osmium.InvalidLocationError:
            return
        if not overlaps_bbox(coords):
            return

        if way.tags.get("natural") == "coastline" and len(coords) > 1:
            self.coastlines.append(LineString(coords))

        road_class = way.tags.get("highway")
        if road_class in {"primary", "secondary"} and len(coords) > 1:
            self.roads.append(LineString(coords))

        if way.id in CAUSEWAY_WAY_IDS and len(coords) > 1:
            self.causeway_roads[way.id] = LineString(coords)

        if way.id in self._poi_way_ids and coords:
            line = LineString(coords)
            center = line.centroid
            self.poi_ways[way.id] = (center.x, center.y)


def find_island(coastlines: list[LineString]) -> Polygon:
    candidates = list(polygonize(unary_union(coastlines)))
    center = Point(10.91, 33.80)
    containing = [polygon for polygon in candidates if polygon.contains(center)]
    if containing:
        return max(containing, key=lambda polygon: polygon.area)

    plausible = [
        polygon
        for polygon in candidates
        if polygon.bounds[0] < 10.90 < polygon.bounds[2]
        and polygon.bounds[1] < 33.80 < polygon.bounds[3]
    ]
    if plausible:
        return max(plausible, key=lambda polygon: polygon.area)
    raise RuntimeError(f"Could not reconstruct Djerba coastline; polygon candidates: {len(candidates)}")


def find_context_land(
    coastlines: list[LineString], island: Polygon, canvas_viewport: Polygon
) -> list[Polygon]:
    """Return mainland reaching the SVG edges and meaningful closed islets."""
    clipped_coastlines = [
        coastline.intersection(canvas_viewport)
        for coastline in coastlines
        if coastline.intersects(canvas_viewport)
    ]
    bounded_candidates = list(
        polygonize(unary_union([*clipped_coastlines, canvas_viewport.boundary]))
    )
    viewport_area = canvas_viewport.area
    frame_west, frame_south, frame_east, frame_north = canvas_viewport.bounds
    mainlands = [
        polygon
        for polygon in bounded_candidates
        if polygon.area >= 0.001
        and polygon.area < viewport_area * 0.2
        and (
            polygon.bounds[0] <= frame_west + 1e-8
            or polygon.bounds[1] <= frame_south + 1e-8
            or polygon.bounds[2] >= frame_east - 1e-8
            or polygon.bounds[3] >= frame_north - 1e-8
        )
    ]

    island_viewport = box(WEST, SOUTH, EAST, NORTH)
    closed_candidates = list(polygonize(unary_union(coastlines)))
    islets = [
        polygon
        for polygon in closed_candidates
        if polygon.area >= MIN_CONTEXT_ISLAND_AREA
        and polygon.area < 0.005
        and polygon.intersects(island_viewport)
        and not polygon.equals(island)
    ]
    return [*mainlands, *islets]


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
    canvas_viewport = box(canvas_west, canvas_south, canvas_east, canvas_north)

    return project, scale, canvas_viewport


def path_data(coords, project, close: bool = False) -> str:
    points = [project(lon, lat) for lon, lat in coords]
    if not points:
        return ""
    parts = [f"M {points[0][0]:.1f} {points[0][1]:.1f}"]
    parts.extend(f"L {x:.1f} {y:.1f}" for x, y in points[1:])
    if close:
        parts.append("Z")
    return " ".join(parts)


def make_svg(data: DjerbaData) -> str:
    source_island = find_island(data.coastlines)
    project, projection_scale, canvas_viewport = projection()
    context_land = [
        polygon.simplify(0.00025, preserve_topology=True)
        for polygon in find_context_land(
            data.coastlines, source_island, canvas_viewport
        )
    ]
    island = source_island.simplify(0.00035, preserve_topology=True)
    island_path = path_data(island.exterior.coords, project, close=True)
    context_land_paths = [
        path_data(polygon.exterior.coords, project, close=True)
        for polygon in context_land
    ]

    road_paths: list[str] = []
    island_buffer = island.buffer(0.0002)
    for road in data.roads:
        clipped = road.intersection(island_buffer)
        if clipped.is_empty:
            continue
        parts = [clipped] if clipped.geom_type == "LineString" else list(clipped.geoms)
        for part in parts:
            simplified = part.simplify(0.00025, preserve_topology=True)
            # Short fragments are mostly roundabouts, slip roads and divided-road
            # joins.  They add visual noise at an island-wide scale.
            if simplified.length < 0.0025:
                continue
            road_paths.append(path_data(simplified.coords, project))

    missing_causeway_ways = CAUSEWAY_WAY_IDS - data.causeway_roads.keys()
    if missing_causeway_ways:
        raise RuntimeError(
            "Missing configured El Kantara road segments: "
            + ", ".join(str(value) for value in sorted(missing_causeway_ways))
        )
    causeway_paths = [
        path_data(
            data.causeway_roads[way_id].simplify(0.0001, preserve_topology=True).coords,
            project,
        )
        for way_id in sorted(CAUSEWAY_WAY_IDS)
    ]

    missing = []
    for item in POIS:
        if "node" in item and item["node"] not in data.poi_nodes:
            missing.append(str(item["node"]))
        if "way" in item and item["way"] not in data.poi_ways:
            missing.append(str(item["way"]))
    if missing:
        raise RuntimeError("Missing configured OSM objects: " + ", ".join(missing))

    poi_layout = []
    for item in POIS:
        lon, lat = data.poi_nodes[item["node"]] if "node" in item else data.poi_ways[item["way"]]
        origin_x, origin_y = project(lon, lat)
        marker_x = origin_x + item.get("marker_dx", 0)
        marker_y = origin_y + item.get("marker_dy", 0)
        label_x = marker_x + item["label_dx"]
        label_y = marker_y + item["label_dy"]
        poi_layout.append(
            {
                "item": item,
                "origin_x": origin_x,
                "origin_y": origin_y,
                "marker_x": marker_x,
                "marker_y": marker_y,
                "label_x": label_x,
                "label_y": label_y,
                "displacement": math.hypot(
                    marker_x - origin_x, marker_y - origin_y
                ),
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
    scale_end_x = VIEW_WIDTH - 68
    scale_start_x = scale_end_x - scale_width
    scale_middle_x = (scale_start_x + scale_end_x) / 2
    scale_y = 690
    mainland_label_x, mainland_label_y = project(10.690, 33.620)
    causeway_label_x, causeway_label_y = project(10.952, 33.666)
    causeway_target_x, causeway_target_y = project(*CAUSEWAY_LABEL_TARGET)

    lines = [
        '<svg class="place-map__graphic" viewBox="0 0 960 760" role="img"',
        '  aria-labelledby="djerba-map-title djerba-map-desc" xmlns="http://www.w3.org/2000/svg">',
        '  <title id="djerba-map-title">Mapa orientacyjna Dżerby: hotel i miejsca z Atlasu</title>',
        '  <desc id="djerba-map-desc">Mapa pokazuje zarys Dżerby, pobliskie wysepki, fragment kontynentalnej Tunezji oraz Groblę El Kantara, zwaną drogą rzymską. Grobla jest jednym połączeniem drogowym, a jej podpis łączy linia z przebiegiem RR117. Hotel Club Palm Azur oznaczono literą H. Numery od 1 do 6 wskazują Houmt Souk, Erriadh i Djerbahood, synagogę El Ghriba, Guellalę, Djerba Explore oraz Ras Rmel. Punkty 2 i 3 dzieli w rzeczywistości około 740 metrów; ich koła są minimalnie rozsunięte, aby się nie stykały. W prawym dolnym rogu znajduje się podziałka od 0 do 10 kilometrów. Szczegółowy opis położenia znajduje się pod mapą.</desc>',
        f'  <metadata>OpenStreetMap snapshot tunisia-260822.osm.pbf, SHA-256 {SNAPSHOT_SHA256}</metadata>',
        '  <defs aria-hidden="true">',
        '    <clipPath id="djerba-map-clip">',
        '      <rect width="960" height="760" rx="12"/>',
        '    </clipPath>',
        '  </defs>',
        '  <rect class="place-map__water" width="960" height="760" rx="12"/>',
        '  <g class="place-map__context-land" clip-path="url(#djerba-map-clip)" aria-hidden="true">',
    ]
    lines.extend(f'    <path d="{value}"/>' for value in context_land_paths if value)
    lines.extend([
        '  </g>',
        f'  <path class="place-map__land" d="{island_path}"/>',
        '  <g class="place-map__roads" aria-hidden="true">',
    ])
    lines.extend(f'    <path d="{value}"/>' for value in road_paths if value)
    lines.extend([
        '  </g>',
        '  <g class="place-map__causeway" aria-hidden="true">',
    ])
    lines.extend(f'    <path d="{value}"/>' for value in causeway_paths if value)
    lines.extend([
        '  </g>',
        '  <g class="place-map__causeway-center" aria-hidden="true">',
    ])
    lines.extend(f'    <path d="{value}"/>' for value in causeway_paths if value)
    lines.extend([
        '  </g>',
        '  <g class="place-map__context" aria-hidden="true">',
        f'    <text class="place-map__geography-label" x="{mainland_label_x:.1f}" y="{mainland_label_y:.1f}" text-anchor="middle">Kontynent – Tunezja</text>',
        f'    <path class="place-map__context-leader" d="M {causeway_target_x:.1f} {causeway_target_y:.1f} L {causeway_label_x - 8:.1f} {causeway_label_y:.1f}"/>',
        f'    <text class="place-map__causeway-label" x="{causeway_label_x:.1f}" y="{causeway_label_y:.1f}" text-anchor="start">',
        '      <tspan x="{:.1f}" dy="0">Grobla El Kantara</tspan>'.format(causeway_label_x),
        '      <tspan x="{:.1f}" dy="19">– droga rzymska</tspan>'.format(causeway_label_x),
        '    </text>',
    ])

    context_offsets = {
        287613682: (12, -12, "start"),
    }
    for node_id, name in CONTEXT_NODES.items():
        lon, lat = data.context_nodes[node_id]
        x, y = project(lon, lat)
        dx, dy, anchor = context_offsets[node_id]
        lines.append(f'    <circle cx="{x:.1f}" cy="{y:.1f}" r="4"/>')
        lines.append(
            f'    <text x="{x + dx:.1f}" y="{y + dy:.1f}" text-anchor="{anchor}">{html.escape(name)}</text>'
        )
    lines.extend([
        '  </g>',
        '  <g class="place-map__points" aria-hidden="true">',
        '    <g class="place-map__leaders">',
    ])

    for point in poi_layout:
        item = point["item"]
        x, y = point["marker_x"], point["marker_y"]
        lx, ly = point["label_x"], point["label_y"]
        if point["displacement"] > MARKER_RADIUS:
            lines.append(
                '      <path class="place-map__location-leader" '
                f'd="M {point["origin_x"]:.1f} {point["origin_y"]:.1f} L {x:.1f} {y:.1f}"/>'
            )
        line_end_x = lx - 8 if item["anchor"] == "start" else lx + 8
        line_end_y = ly - 5
        lines.append(
            f'      <path class="place-map__leader" d="M {x:.1f} {y:.1f} L {line_end_x:.1f} {line_end_y:.1f}"/>'
        )

    lines.append('    </g>')
    displaced_points = [
        point for point in poi_layout if point["displacement"] > MARKER_RADIUS
    ]
    if displaced_points:
        lines.append('    <g class="place-map__origins">')
        for point in displaced_points:
            lines.append(
                f'      <circle cx="{point["origin_x"]:.1f}" cy="{point["origin_y"]:.1f}" r="3"/>'
            )
        lines.append('    </g>')
    lines.append('    <g class="place-map__markers">')

    for point in poi_layout:
        item = point["item"]
        x, y = point["marker_x"], point["marker_y"]
        marker_class = "place-map__marker place-map__marker--hotel" if item["kind"] == "hotel" else "place-map__marker"
        lines.append(f'    <g class="{marker_class}">')
        if item["kind"] == "hotel":
            size = MARKER_RADIUS
            points = f"{x:.1f},{y-size:.1f} {x+size:.1f},{y:.1f} {x:.1f},{y+size:.1f} {x-size:.1f},{y:.1f}"
            lines.append(f'      <polygon points="{points}"/>')
        else:
            lines.append(f'      <circle cx="{x:.1f}" cy="{y:.1f}" r="{MARKER_RADIUS}"/>')
        lines.append(f'      <text class="place-map__marker-text" x="{x:.1f}" y="{y + 5.5:.1f}" text-anchor="middle">{item["number"]}</text>')
        lines.append('    </g>')

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
        '  </g>',
        '  <g class="place-map__scale" aria-hidden="true">',
        f'    <text x="{scale_middle_x:.1f}" y="666" text-anchor="middle">Skala</text>',
        f'    <path d="M {scale_start_x:.1f} {scale_y:.1f} H {scale_end_x:.1f} M {scale_start_x:.1f} {scale_y - 10:.1f} V {scale_y + 10:.1f} M {scale_middle_x:.1f} {scale_y - 7:.1f} V {scale_y + 7:.1f} M {scale_end_x:.1f} {scale_y - 10:.1f} V {scale_y + 10:.1f}"/>',
        f'    <text x="{scale_start_x:.1f}" y="718" text-anchor="middle">0</text>',
        f'    <text x="{scale_middle_x:.1f}" y="718" text-anchor="middle">5</text>',
        f'    <text x="{scale_end_x:.1f}" y="718" text-anchor="middle">10 km</text>',
        '  </g>',
        '  <g class="place-map__north" aria-hidden="true" transform="translate(890 78)">',
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

    data = DjerbaData()
    data.apply_file(str(args.pbf), locations=True)
    output = make_svg(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
