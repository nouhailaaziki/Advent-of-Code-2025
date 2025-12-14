import sys

TARGET = 12

def max_k_digits(s, k):
    s = s.strip()
    need = k
    stack = []
    remaining = len(s)

    for ch in s:
        d = ord(ch) - 48
        while stack and stack[-1] < d and (len(stack) - 1 + remaining) >= need:
            stack.pop()
        stack.append(d)
        remaining -= 1

    if len(stack) > k:
        stack = stack[:k]

    return "".join(str(x) for x in stack)

def main():
    total = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        best = max_k_digits(line, TARGET)
        total += int(best)

    print(total)

if __name__ == "__main__":
    main()
