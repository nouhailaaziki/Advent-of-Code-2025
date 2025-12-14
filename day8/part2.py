import sys

class DSU(object):
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, a):
        p = self.parent
        while p[a] != a:
            p[a] = p[p[a]]
            a = p[a]
        return a

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True

def parse_points(lines):
    pts = []
    for line in lines:
        s = line.strip()
        if not s:
            continue
        parts = s.split(',')
        if len(parts) != 3:
            raise ValueError("Bad line (expected X,Y,Z): " + repr(line))
        x = int(parts[0].strip())
        y = int(parts[1].strip())
        z = int(parts[2].strip())
        pts.append((x, y, z))
    return pts

def last_connection_product(points):
    n = len(points)
    if n <= 1:
        return 0

    pairs = []
    for i in range(n):
        xi, yi, zi = points[i]
        for j in range(i+1, n):
            xj, yj, zj = points[j]
            dx = xi - xj
            dy = yi - yj
            dz = zi - zj
            dist2 = dx*dx + dy*dy + dz*dz
            pairs.append((dist2, i, j))

    pairs.sort(key=lambda t: t[0])

    dsu = DSU(n)

    for dist2, i, j in pairs:
        if dsu.union(i, j):
            if dsu.components == 1:
                return points[i][0] * points[j][0]

    return 0

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.read().splitlines()

    points = parse_points(lines)
    result = last_connection_product(points)
    print(result)

if __name__ == "__main__":
    main()
