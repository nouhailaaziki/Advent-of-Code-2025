from pathlib import Path
from typing import List, Set, Tuple
import pulp


def parse_input(path: str) -> List[Tuple[List[bool], List[Set[int]], List[int]]]:
    text = Path(path).read_text().strip().splitlines()
    tasks = []
    for line in text:
        parts = line.split()
        toggles_token, *button_tokens, counters_token = parts
        toggles = [c == "#" for c in toggles_token[1:-1]]
        moves = [set(map(int, bt[1:-1].split(","))) for bt in button_tokens]
        counters = list(map(int, counters_token[1:-1].split(",")))
        tasks.append((toggles, moves, counters))
    return tasks


def solve(goal: List[int], moves: List[Set[int]], part1: bool) -> float:

    m = len(goal)
    n = len(moves)

    prob = pulp.LpProblem("min_moves", pulp.LpMinimize)

    x = [pulp.LpVariable(f"x_{i}", lowBound=0, cat="Integer") for i in range(n)]

    s = [None] * m
    if part1:
        for j in range(m):
            s[j] = pulp.LpVariable(f"s_{j}", lowBound=None, upBound=None, cat="Integer")

    prob += pulp.lpSum(x), "total_moves"

    for j in range(m):
        coeff_sum = pulp.lpSum(x[i] for i in range(n) if j in moves[i])
        if part1:
            prob += coeff_sum + (-2) * s[j] == goal[j], f"counter_eq_{j}"
        else:
            prob += coeff_sum == goal[j], f"counter_eq_{j}"

    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    obj = pulp.value(prob.objective)
    if obj is None:
        raise RuntimeError("Solver failed to find a solution")
    return obj


if __name__ == "__main__":
    tasks = parse_input("puzzle_input")
    total = sum(solve(goal, moves, part1=False) for _, moves, goal in tasks)
    if abs(round(total) - total) < 1e-9:
        print(int(round(total)))
    else:
        print(total)