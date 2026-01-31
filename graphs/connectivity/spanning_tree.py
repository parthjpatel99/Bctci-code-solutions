"""
Given the adjacency list of an undirected, connected graph, graph, return a set of edges forming a spanning tree.

A spanning tree is a subset of edges that connects (i.e., "spans") every node and has no cycles.

Example 1:
graph = [
  [1],
  [0, 2, 5],
  [1, 3, 4],
  [2],
  [2, 5],
  [1, 4]
]
Output: [[0, 1], [1, 2], [2, 3], [2, 4], [4, 5]]
There are other valid answers

Example 2:
graph = [[1], [0]]
Output: [[0, 1]]
A single edge is a valid spanning tree for two nodes.

Example 3:
graph = [
  [1, 2],
  [0, 2],
  [0, 1]
]
Output: [[0, 1], [0, 2]]
There are other valid answers, like [[0, 1], [1, 2]].

Example 4:
graph = [[]]
Output: []
This graph has a single node and no edges.

Constraints:

    1 ≤ graph.length ≤ 1000
    graph[i].length < 1000
    0 ≤ graph[i][j] < graph.length
    The adjacency list is properly formatted, with no parallel edges or self-loops
    The graph is connected
"""


def spanning_tree(graph):
    V = len(graph)
    visited = set()
    predecessors = {}

    def dfs(node):
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                predecessors[nbr] = node
                dfs(nbr)

    dfs(0)
    edges = []
    for node, pred in predecessors.items():
        edges.append([pred, node])
    return edges


def run_tests():
    class Colors:
        GREEN = "\033[92m"
        RED = "\033[91m"
        END = "\033[0m"

    tests = [
        ([[1], [0, 2, 5], [1, 3, 4], [2], [2, 5], [1, 4]], "Book example"),
        ([[1], [0]], "Single edge"),
        ([[1], [0, 2], [1]], "Line graph"),
        ([[1, 2, 3], [0], [0], [0]], "Star graph"),
        ([[1, 2], [0, 2], [0, 1]], "Complete graph"),
        ([[]], "Single node graph"),
    ]

    passed = 0
    print("Running spanning_tree() Tests...\n")

    for idx, (graph, desc) in enumerate(tests):
        ok = True
        got = spanning_tree(graph)
        V = len(graph)

        # 1. Correct number of edges
        if len(got) != V - 1:
            ok = False
            reason = f"Wrong number of edges: expected {V-1}, got {len(got)}"

        # 2. Edges are valid
        if ok:
            for u, v in got:
                if not (0 <= u < V and 0 <= v < V):
                    ok = False
                    reason = f"Invalid node in edge {[u,v]}"
                    break
                if v not in graph[u] or u not in graph[v]:
                    ok = False
                    reason = f"Invalid edge {[u,v]} not in graph"
                    break

        # 3. Edges form a tree (no cycles + connected)
        if ok and V > 0:
            adj = [[] for _ in range(V)]
            for u, v in got:
                adj[u].append(v)
                adj[v].append(u)

            visited = set()

            def dfs(node, parent):
                visited.add(node)
                for nbr in adj[node]:
                    if nbr != parent:
                        if nbr in visited or not dfs(nbr, node):
                            return False
                return True

            if not dfs(0, -1) or len(visited) != V:
                ok = False
                reason = f"Edges do not form a valid tree: {got}"

        # Output result
        status = "✅ PASSED" if ok else "❌ FAILED"
        color = Colors.GREEN if ok else Colors.RED
        print(f"Test {idx + 1}: {color}{status}{Colors.END}")
        print(f"  Description     : {desc}")
        print(f"  Graph           : {graph}")
        print(f"  Spanning Tree   : {got}")
        if not ok:
            print(f"  Reason          : {reason}")
        print("-" * 40)

        if ok:
            passed += 1

    total = len(tests)
    print(f"\nSummary: {passed}/{total} tests passed.")
    if passed == total:
        print(f"{Colors.GREEN}🎉 All tests passed!{Colors.END}")
    else:
        print(f"{Colors.RED}Some tests failed. Please review above.{Colors.END}")


run_tests()
