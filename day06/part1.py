import sys

def main():
    lines = [r.rstrip("\n") for r in sys.stdin]
    if not lines:
        print(0)
        return

    width = max(len(r) for r in lines)
    lines = [r.ljust(width) for r in lines]

    is_space_col = [all(row[c] == " " for row in lines) for c in range(width)]

    blocks = []
    c = 0
    while c < width:
        if is_space_col[c]:
            c += 1
            continue
        start = c
        while c < width and not is_space_col[c]:
            c += 1
        blocks.append((start, c))
        
    total_sum = 0

    for (start, end) in blocks:
        col_slice = [row[start:end] for row in lines]

        op_line = col_slice[-1].strip()
        if op_line not in ("+", "*"):
            continue
        op = op_line

        nums = []
        for row in col_slice[:-1]:
            s = row.strip()
            if s != "":
                nums.append(int(s))

        if not nums:
            continue

        if op == "+":
            res = sum(nums)
        else:
            res = 1
            for x in nums:
                res *= x

        total_sum += res

    print(total_sum)

if __name__ == "__main__":
    main()
