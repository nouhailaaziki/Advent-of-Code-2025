import sys
import os


def is_invalid_id(n):
    s = str(n)
    l = len(s)
    if l % 2 != 0:
        return False
    half = l // 2
    return s[:half] == s[half:]


def sum_invalid_ids(ranges_line):
    total = 0
    ranges = ranges_line.strip().split(',')
    for r in ranges:
        if not r:
            continue
        start, end = map(int, r.split('-'))
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n
    return total


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = os.path.join(os.path.dirname(__file__), 'puzzle_input')

    try:
        with open(path, 'r') as f:
            input_ranges = f.read().strip()
    except Exception as e:
        sys.stderr.write("Error reading input file {}: {}\n".format(path, e))
        sys.exit(1)

    print(sum_invalid_ids(input_ranges))


if __name__ == '__main__':
    main()

