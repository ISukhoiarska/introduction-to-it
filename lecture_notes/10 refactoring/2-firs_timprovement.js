'use strict';

const shift = (offset, points) => {   ///change let into const
    for (const point of points) {     ///changed loop forEach into for
        const type = typeof point;
        if (type === 'object') {
            point.x += offset.x;
            point.y += offset.y;
        } else {
            const i = points.indexOf(point);    ///changed let into const
            points[i] = JSON.parse(point);
            points[i].x += offset.x;
            points[i].y += offset.y;
        }
    }
    return points;
};

const polyline = [
    { x: 0, y: 0 },
    { x: 10, y: 10 },
    '{ "x": 20, "y": 20 }',
    { x: 30, y: 30 },
];

const shifted = shift({ x: 10, y: -5 }, polyline);
console.log({ shifted });
