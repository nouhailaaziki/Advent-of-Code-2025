import sys

def parse_input(lines):
    shapes = {}
    regions = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if ':' in line and line[:-1].isdigit():
            idx = int(line[:-1])
            i += 1
            area = 0
            while i < len(lines) and lines[i].strip():
                area += lines[i].count('#')
                i += 1
            shapes[idx] = area
        else:
            break

    while i < len(lines):
        line = lines[i].strip()
        if line:
            size, counts = line.split(':')
            w, h = map(int, size.split('x'))
            nums = list(map(int, counts.strip().split()))
            regions.append((w * h, nums))
        i += 1

    return shapes, regions


def count_valid_regions(shapes, regions):
    valid = 0
    for area, nums in regions:
        needed = 0
        for i, c in enumerate(nums):
            needed += c * shapes[i]
        if needed <= area:
            valid += 1
    return valid


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    shapes, regions = parse_input(lines)
    print(count_valid_regions(shapes, regions))
