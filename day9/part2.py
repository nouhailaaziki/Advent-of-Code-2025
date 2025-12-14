from itertools import combinations
from shapely.geometry import Polygon, box

def read_points(path):
    with open(path) as f:
        tokens = f.read().strip().split()
    return [tuple(map(int, t.split(","))) for t in tokens]

def inclusive_area(xmin, ymin, xmax, ymax):
    return (xmax - xmin + 1) * (ymax - ymin + 1)

def max_contained_rectangle_area(points):
    poly = Polygon(points)

    contained_areas = (
        inclusive_area(xmin, ymin, xmax, ymax)
        for (x1, y1), (x2, y2) in combinations(points, 2)
        for xmin, xmax in [(min(x1, x2), max(x1, x2))]
        for ymin, ymax in [(min(y1, y2), max(y1, y2))]
        if poly.contains(box(xmin, ymin, xmax, ymax))
    )

    return max(contained_areas)

if __name__ == "__main__":
    points = read_points("puzzle_input")
    print(max_contained_rectangle_area(points))