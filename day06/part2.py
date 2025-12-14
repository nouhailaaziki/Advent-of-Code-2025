def cephalopod_math(grid):
    rows = [line.rstrip('\n') for line in grid.strip().split('\n')]
    num_rows = len(rows)
    num_cols = max(len(row) for row in rows)
    rows = [row.ljust(num_cols) for row in rows]

    grand_total = 0
    c = 0

    while c < num_cols:
        if all(rows[r][c] == ' ' for r in range(num_rows)):
            c += 1
            continue

        problem_cols = []
        while c < num_cols and not all(rows[r][c] == ' ' for r in range(num_rows)):
            problem_cols.append([rows[r][c] for r in range(num_rows)])
            c += 1

        bottom_row = [col[-1] for col in problem_cols]
        operator = None
        for ch in reversed(bottom_row):
            if ch in '+*':
                operator = ch
                break
        if operator is None:
            raise ValueError("No operator found in problem.")

        numbers = []
        for col in reversed(problem_cols):
            digits = col[:-1] if col[-1] != operator else col[:-1]
            digits = [ch for ch in digits if ch != ' ']
            num_str = ''.join(digits)
            if num_str == '':
                numbers.append(0)
            else:
                numbers.append(int(num_str))

        if operator == '+':
            result = sum(numbers)
        else:
            result = 1
            for n in numbers:
                result *= n

        grand_total += result

    return grand_total


if __name__ == '__main__':
    try:
        with open('puzzle_input', 'r', encoding='utf-8') as f:
            worksheet = f.read()
    except FileNotFoundError:
        raise SystemExit("puzzle_input file not found.")

    print(cephalopod_math(worksheet))
