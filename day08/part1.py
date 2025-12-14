import sys
from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

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

def product_of_top_three_component_sizes(points, k=1000):
    n = len(points)
    if n == 0:
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

    use = min(k, len(pairs))
    dsu = DSU(n)

    for idx in range(use):
        _, i, j = pairs[idx]
        dsu.union(i, j)

    comp_count = defaultdict(int)
    for i in range(n):
        root = dsu.find(i)
        comp_count[root] += 1

    sizes = sorted(comp_count.values(), reverse=True)

    while len(sizes) < 3:
        sizes.append(1)

    return sizes[0] * sizes[1] * sizes[2]

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Connect the k shortest pairs among 3D points and multiply sizes of top 3 components.")
    parser.add_argument("file", nargs="?", help="input file (default: stdin)")
    parser.add_argument("-k", type=int, default=1000, help="number of shortest pairs to process")
    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.read().splitlines()

    points = parse_points(lines)
    result = product_of_top_three_component_sizes(points, k=args.k)
    print(result)

if __name__ == "__main__":
    main()
