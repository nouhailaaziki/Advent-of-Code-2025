def count_timelines(grid):
    rows = len(grid)
    cols = len(grid[0])

    dp = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                dp[r][c] = 1
                break

    for r in range(rows - 1):
        for c in range(cols):
            if dp[r][c] == 0:
                continue
            cell = grid[r][c]
            if cell == '.' or cell == 'S' or cell == '|':
                dp[r + 1][c] += dp[r][c]
            elif cell == '^':
                if c - 1 >= 0:
                    dp[r + 1][c - 1] += dp[r][c]
                if c + 1 < cols:
                    dp[r + 1][c + 1] += dp[r][c]

    return sum(dp[rows - 1])


def load_input():
    from pathlib import Path
    p = Path(__file__).parent / "puzzle_input"
    if not p.exists():
        p = Path("puzzle_input")
    if not p.exists():
        raise FileNotFoundError(f"puzzle_input not found at {p}")
    lines = [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln != ""]
    return lines


if __name__ == "__main__":
    grid = load_input()
    print(count_timelines(grid))