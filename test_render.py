"""Offline self-check: render a synthetic scene, no network needed. Run: python test_render.py"""

import geopandas as gpd
from shapely import LineString, Point, Polygon

import mapart


def synthetic_scene():
    center, dist = (52.5, 13.4), 600
    feats = gpd.GeoDataFrame(
        {
            "building": ["yes", "yes", None, None, None],
            "natural": [None, None, "water", "wood", None],
            "water": [None, None, None, None, None],
            "waterway": [None, None, None, None, "river"],
            "leisure": [None, None, None, None, "park"],
            "landuse": [None, None, None, None, None],
            "geometry": [
                Polygon(
                    [
                        (13.398, 52.501),
                        (13.399, 52.501),
                        (13.399, 52.502),
                        (13.398, 52.502),
                    ]
                ),
                Polygon(
                    [
                        (13.401, 52.499),
                        (13.402, 52.499),
                        (13.402, 52.500),
                        (13.401, 52.500),
                    ]
                ),
                Polygon(
                    [
                        (13.403, 52.502),
                        (13.406, 52.502),
                        (13.406, 52.504),
                        (13.403, 52.504),
                    ]
                ),
                Polygon(
                    [
                        (13.394, 52.496),
                        (13.398, 52.496),
                        (13.398, 52.499),
                        (13.394, 52.499),
                    ]
                ),
                Polygon(
                    [
                        (13.400, 52.503),
                        (13.403, 52.503),
                        (13.403, 52.505),
                        (13.400, 52.505),
                    ]
                ),
            ],
        },
        crs="EPSG:4326",
    )
    edges = gpd.GeoDataFrame(
        {
            "highway": ["primary", "residential", "service"],
            "geometry": [
                LineString([(13.39, 52.500), (13.41, 52.5005)]),
                LineString([(13.400, 52.49), (13.4005, 52.51)]),
                LineString([(13.395, 52.504), (13.402, 52.506)]),
            ],
        },
        crs="EPSG:4326",
    )
    return feats, edges, center, dist


def test_render():
    feats, edges, center, dist = synthetic_scene()
    for name, style in mapart.PRESETS.items():
        for circle in (True, False):
            png = mapart.render_scene(
                feats, edges, center, dist, style, size=500, circle=circle
            )
            assert png[:8] == b"\x89PNG\r\n\x1a\n", name
            assert len(png) > 1000, name
    print(f"ok: {len(mapart.PRESETS)} presets x 2 shapes render valid PNGs")


if __name__ == "__main__":
    test_render()
