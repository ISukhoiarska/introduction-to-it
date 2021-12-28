import json


def type_of_element(point):
    point = json.loads(point)
    return point


def shift(offset, points):
    for i in range(0, len(points), 1):
        if type(points[i]) == str:
            points[i] = type_of_element(points[i])
        points[i]["x"] += offset["x"]
        points[i]["y"] += offset["y"]
    return points


polyline = [
    {'x': 0, 'y': 0},
    {'x': 10, 'y': 10},
    '{"x": 20, "y": 20}',
    {'x': 30, 'y': 30}
]

shift({'x': 10, 'y': -5}, polyline)
print(polyline)
