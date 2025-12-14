import sys

def main():
    lines = [line.strip() for line in sys.stdin]

    parts = []
    current = []
    for line in lines:
        if line == "":
            parts.append(current)
            current = []
        else:
            current.append(line)
    parts.append(current)

    if not parts or not parts[0]:
        print(0)
        return

    ranges_raw = parts[0]

    intervals = []
    for r in ranges_raw:
        a, b = r.split("-")
        intervals.append((int(a), int(b)))

    intervals.sort()

    merged = []
    s, e = intervals[0]

    for a, b in intervals[1:]:
        if a <= e + 1:
            if b > e:
                e = b
        else:
            merged.append((s, e))
            s, e = a, b

    merged.append((s, e))

    total = 0
    for a, b in merged:
        total += (b - a + 1)

    print(total)

if __name__ == "__main__":
    main()
