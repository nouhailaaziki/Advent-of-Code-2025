import sys

def largest_rectangle(points):
    n = len(points)
    max_area = 0

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]

            width  = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1

            area = width * height

            if area > max_area:
                max_area = area

    return max_area


if __name__ == "__main__":
    pts = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        x, y = map(int, line.split(","))
        pts.append((x, y))

    print(largest_rectangle(pts))
