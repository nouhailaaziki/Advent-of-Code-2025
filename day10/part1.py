import sys
import re

def popcount(x):
    return bin(x).count('1')

def parse_line(line):
    line = line.strip()
    if not line:
        return None
    pattern = re.search(r'\[([.#]+)\]', line)
    if not pattern:
        return None
    lights = pattern.group(1)
    m = len(lights)
    b = [1 if c == '#' else 0 for c in lights]

    buttons = re.findall(r'\(([0-9,\s]*)\)', line)
    btn_lists = []
    for btn in buttons:
        if btn.strip() == "":
            btn_lists.append([])
        else:
            nums = [int(x) for x in btn.split(',') if x.strip()!='']
            btn_lists.append(nums)

    return m, b, btn_lists

def solve_one(m, b_list, btn_lists):
    n = len(btn_lists)
    if n == 0:
        if any(b_list):
            return None
        else:
            return 0

    rows = [0] * m
    rhs = [0] * m
    for i in range(m):
        rhs[i] = b_list[i]
    for j, bl in enumerate(btn_lists):
        for idx in bl:
            if 0 <= idx < m:
                rows[idx] |= (1 << j)

    pivot_for_col = [-1] * n
    row = 0
    for col in range(n):
        sel = -1
        for r in range(row, m):
            if (rows[r] >> col) & 1:
                sel = r
                break
        if sel == -1:
            continue
        # swap
        rows[row], rows[sel] = rows[sel], rows[row]
        rhs[row], rhs[sel] = rhs[sel], rhs[row]
        pivot_for_col[col] = row

        for r in range(m):
            if r != row and ((rows[r] >> col) & 1):
                rows[r] ^= rows[row]
                rhs[r] ^= rhs[row]
        row += 1
        if row >= m:
            break

    for r in range(m):
        if rows[r] == 0 and rhs[r] == 1:
            return None

    x0 = [0] * n
    for col in range(n-1, -1, -1):
        prow = pivot_for_col[col]
        if prow == -1:
            continue
        mask = rows[prow]
        mask_no_pivot = mask & (~(1 << col))
        s = 0
        mm = mask_no_pivot
        while mm:
            lsb = mm & -mm
            j = (lsb.bit_length() - 1)
            s ^= x0[j]
            mm ^= lsb
        x0[col] = rhs[prow] ^ s

    free_cols = [j for j in range(n) if pivot_for_col[j] == -1]
    f = len(free_cols)

    basis = []
    for idx, fc in enumerate(free_cols):
        vec = 0
        vec |= (1 << fc)
        for col in range(n):
            prow = pivot_for_col[col]
            if prow != -1:
                if (rows[prow] >> fc) & 1:
                    vec |= (1 << col)
        basis.append(vec)

    x0_mask = 0
    for j in range(n):
        if x0[j]:
            x0_mask |= (1 << j)

    if f == 0:
        return popcount(x0_mask)

    THRESH = 22
    best = None
    if f <= THRESH:
        total = 1 << f
        for s in range(total):
            mask = x0_mask
            i = 0
            ss = s
            while ss:
                lsb = ss & -ss
                j = (lsb.bit_length() - 1)
                mask ^= basis[j]
                ss ^= lsb
            c = popcount(mask)
            if best is None or c < best:
                best = c
    else:
        f1 = f // 2
        f2 = f - f1
        first = {}
        total1 = 1 << f1
        for s in range(total1):
            mask = 0
            ss = s
            j = 0
            while ss:
                lsb = ss & -ss
                idx = (lsb.bit_length() - 1)
                mask ^= basis[idx]
                ss ^= lsb
            first[mask] = min(first.get(mask, 999999), popcount((x0_mask) ^ mask))

        first_items = first.items()

        total2 = 1 << f2
        for s in range(total2):
            mask2 = 0
            ss = s
            while ss:
                lsb = ss & -ss
                idx = (lsb.bit_length() - 1) + f1
                mask2 ^= basis[idx]
                ss ^= lsb
            target = x0_mask ^ mask2
            for mask1, basecount in first_items:
                c = popcount(target ^ mask1)
                if best is None or c < best:
                    best = c

    return best

def main():
    data = sys.stdin.read().strip().splitlines()
    total = 0
    any_impossible = False
    for line in data:
        parsed = parse_line(line)
        if not parsed:
            continue
        m, b, btns = parsed
        res = solve_one(m, b, btns)
        if res is None:
            any_impossible = True
            print("IMPOSSIBLE")
            return
        total += res
    print(total)

if __name__ == '__main__':
    main()
