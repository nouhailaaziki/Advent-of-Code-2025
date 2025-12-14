from pathlib import Path

def load_graph(path="puzzle_input"):
    adj = {}
    for line in Path(path).read_text().strip().splitlines():
        if not line or line.strip().startswith("#"):
            continue
        left, right = line.split(":", 1)
        node = left.strip()
        targets = right.strip()
        adj[node] = targets.split() if targets else []
    return adj

def count_paths(adj, start="you", goal="out"):
    memo = {}
    visiting = set()

    def dfs(node):
        if node == goal:
            return 1
        if node in memo:
            return memo[node]
        if node in visiting:
            return 0
        visiting.add(node)
        total = sum(dfs(nxt) for nxt in adj.get(node, []))
        visiting.remove(node)
        memo[node] = total
        return total

    return dfs(start)

if __name__ == "__main__":
    graph = load_graph("puzzle_input")
    print(count_paths(graph, "you", "out"))