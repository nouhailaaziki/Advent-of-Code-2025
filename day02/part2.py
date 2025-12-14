import re
import sys
import os

def is_invalid(n):
    s = str(n)
    length = len(s)
    for i in range(1, length // 2 + 1):
        if length % i == 0:
            if s[:i] * (length // i) == s:
                return True
    return False


def read_ranges(filename="puzzle_input"):

    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    nums = re.findall(r"\d+", text)
    nums = list(map(int, nums))
    if len(nums) % 2 != 0:
        raise ValueError("Expected an even number of integers")
    return [(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)]


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "puzzle_input"
    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' not found.")
        sys.exit(1)

    ranges = read_ranges(input_file)

    total_invalid = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            if is_invalid(n):
                total_invalid += n

    print(total_invalid)