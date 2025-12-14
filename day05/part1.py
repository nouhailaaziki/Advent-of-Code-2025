import sys

def main():
    lines = [line.strip() for line in sys.stdin]
    if not lines:
        print(0)
        return

    parts = []
    current = []
    for line in lines:
        if line == "":
            parts.append(current)
            current = []
        else:
            current.append(line)
    parts.append(current)

    if len(parts) < 2:
        print(0)
        return

    ranges_raw = parts[0]
    ids_raw = parts[1]

    ranges = []
    for r in ranges_raw:
        a, b = r.split('-')
        ranges.append((int(a), int(b)))

    fresh_count = 0

    for x in ids_raw:
        val = int(x)
        fresh = False
        for a, b in ranges:
            if a <= val <= b:
                fresh = True
                break
        if fresh:
            fresh_count += 1

    print(fresh_count)

if __name__ == "__main__":
    main()
