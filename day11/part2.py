from functools import lru_cache

def load_successors(filename="puzzle_input"):
    succ = {}
    with open(filename) as f:
        for line in f:
            parts = line.split()
            if not parts:
                continue
            start = parts[0].rstrip(":")
            succ[start] = parts[1:]
    return succ

succ = load_successors()

SPECIALS = {"dac", "fft"}

@lru_cache(maxsize=None)
def count_paths(node: str, seen: frozenset) -> int:
    seen = seen | (frozenset((node,)) & SPECIALS)
    if node == "out":
        return 1 if SPECIALS.issubset(seen) else 0
    total = 0
    for nxt in succ.get(node, ()):
        total += count_paths(nxt, seen)
    return total

if __name__ == "__main__":
    print(count_paths("svr", frozenset()))