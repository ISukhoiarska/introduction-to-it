import json


def type_of_element(point):
    return point if (type(point) == dict) else json.loads(point)


def shift(offset, points):
    new_points = []
    for point in points:
        points["x"] += offset["x"]
        points["y"] += offset["y"]
        new_points.append(point)
    return new_points


polyline = [
    {'x': 0, 'y': 0},
    {'x': 10, 'y': 10},
    '{"x": 20, "y": 20}',
    {'x': 30, 'y': 30}
]

shift({'x': 10, 'y': -5}, polyline)
print(polyline)
