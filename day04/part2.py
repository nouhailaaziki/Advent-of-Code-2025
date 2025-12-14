import sys

DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

def count_adjacent_at(grid, r, c, h, w):
    cnt = 0
    for dr, dc in DIRS:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < h and 0 <= nc < w:
            if grid[nr][nc] == '@':
                cnt += 1
    return cnt

def main():
    grid = [list(line.rstrip("\n")) for line in sys.stdin if line.strip()]
    if not grid:
        print(0)
        return

    h = len(grid)
    w = len(grid[0])

    removed_total = 0

    while True:
        to_remove = []

        for r in range(h):
            for c in range(w):
                if grid[r][c] != '@':
                    continue
                adj = count_adjacent_at(grid, r, c, h, w)
                if adj < 4:
                    to_remove.append((r, c))

        if not to_remove:
            break
        for r, c in to_remove:
            grid[r][c] = '.'

        removed_total += len(to_remove)

    print(removed_total)

if __name__ == "__main__":
    main()
