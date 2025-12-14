import sys

DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

def main():
    grid = [list(line.rstrip('\n')) for line in sys.stdin if line.strip()]

    if not grid:
        return

    h = len(grid)
    w = len(grid[0])

    result = [row[:] for row in grid]
    count = 0

    for r in range(h):
        for c in range(w):
            if grid[r][c] != '@':
                continue

            adj = 0
            for dr, dc in DIRS:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < h and 0 <= nc < w:
                    if grid[nr][nc] == '@':
                        adj += 1

            if adj < 4:
                result[r][c] = 'x'
                count += 1

    for row in result:
        print("".join(row))

    print(count)

if __name__ == "__main__":
    main()
