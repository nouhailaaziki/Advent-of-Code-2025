import sys

def max_two_digit(s):
    s = s.strip()
    best = 0
    n = len(s)
    for i in range(n - 1):
        a = ord(s[i]) - 48
        for j in range(i + 1, n):
            b = ord(s[j]) - 48
            val = a * 10 + b
            if val > best:
                best = val
    return best

def main():
    total = 0
    for line in sys.stdin:
        line = line.strip()
        if line:
            total += max_two_digit(line)
    print(total)

if __name__ == "__main__":
    main()
