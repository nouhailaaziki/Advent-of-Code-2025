def count_splits(manifold):
    rows = len(manifold)
    cols = len(manifold[0])

    for c in range(cols):
        if manifold[0][c] == 'S':
            start_col = c
            break

    active_beams = {(0, start_col)}
    split_count = 0

    while active_beams:
        new_beams = set()
        for r, c in active_beams:
            if r + 1 >= rows:
                continue

            next_cell = manifold[r + 1][c]
            if next_cell == '.':
                new_beams.add((r + 1, c))
            elif next_cell == '^':
                split_count += 1
                if c - 1 >= 0:
                    new_beams.add((r + 1, c - 1))
                if c + 1 < cols:
                    new_beams.add((r + 1, c + 1))
            else:
                new_beams.add((r + 1, c))
        active_beams = new_beams

    return split_count


def read_puzzle_input(path="puzzle_input"):

    with open(path, "r") as f:
        return [line.rstrip("\n") for line in f if line.strip()]


if __name__ == "__main__":
    import sys

    input_path = sys.argv[1] if len(sys.argv) > 1 else "puzzle_input"
    manifold = read_puzzle_input(input_path)
    print(count_splits(manifold))