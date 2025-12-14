import sys

dial = 50
countZero = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    dir = line[0]
    dist = int(line[1:])

    if dir == 'R':
        dial = (dial + dist) % 100
    elif dir == 'L':
        dial = (dial - dist) % 100
        if dial < 0:
            dial += 100

    if dial == 0:
        countZero += 1

print countZero
