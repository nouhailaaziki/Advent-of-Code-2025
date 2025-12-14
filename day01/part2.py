from pathlib import Path
import sys

def count_zero_clicks(rotations):
    pos = 50
    zero_hits = 0

    for direction, steps in rotations:
        for _ in range(steps):
            if direction == 'L':
                pos = (pos - 1) % 100
            elif direction == 'R':
                pos = (pos + 1) % 100

            if pos == 0:
                zero_hits += 1

    return zero_hits

def parse_input(text):

    rotations = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        dir_char = line[0].upper()
        if dir_char not in ('L', 'R'):
            raise ValueError(f"unexpected direction in line: {line!r}")
        steps = int(line[1:].strip())
        rotations.append((dir_char, steps))
    return rotations

def main():
    here = Path(__file__).parent
    input_path = here / "puzzle_input"

    if not input_path.exists():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    text = input_path.read_text(encoding="utf-8")
    rotations = parse_input(text)
    result = count_zero_clicks(rotations)
    print(result)

if __name__ == "__main__":
    main()