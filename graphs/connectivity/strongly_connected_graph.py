"""
Given the adjacency list of a non-empty directed graph, graph, return whether it is strongly connected.

A directed graph is strongly connected if every node can reach every other node (in a directed graph, it is possible that node1 can reach node2 but not the other way around).

Below is an image of strongly connected, weakly connected, and disconnected directed graphs. A directed graph is weakly connected if it would be connected if edges didn't have directions.
Strongly Connected Graph

Example 1:
graph = [
  [1, 3],    # Node 0
  [2],       # Node 1
  [0],       # Node 2
  [2]        # Node 3
]

Output: True
Left graph in the image above

Example 2:
graph = [
  [1, 2, 3], # Node 0
  [2],       # Node 1
  [],        # Node 2
  [2]        # Node 3
]

Output: False
Middle graph in the image above
Node 2 cannot reach node 0, among others

Example 3:
graph = [
  [1],       # Node 0
  [0],       # Node 1
  [3],       # Node 2
  [2]        # Node 3
]

Output: False
Right graph in the image above
Node 0 cannot reach node 3, among others

Constraints:

    1 ≤ graph.length ≤ 1000
    graph[i].length < 1000
    0 ≤ graph[i][j] < graph.length
    The adjacency list is properly formatted, with no parallel edges or self-loops
    The graph is directed
"""


def strongly_connected(graph):
    V = len(graph)
    visited = set()

    def dfs(node, agraph, avisited):
        if node in avisited:
            return
        avisited.add(node)

        for nbr in agraph[node]:
            if nbr not in avisited:
                dfs(nbr, agraph, avisited)

    dfs(0, graph, visited)

    if len(visited) < V:
        return False

    reverse_graph = [[] for _ in range(V)]

    for node in range(V):
        for nbr in graph[node]:
            reverse_graph[nbr].append(node)

    reverse_visited = set()
    dfs(0, reverse_graph, reverse_visited)

    return len(reverse_visited) == V


def run_tests():
    class Colors:
        GREEN = "\033[92m"
        RED = "\033[91m"
        END = "\033[0m"

    tests = [
        # Example strongly connected
        ([[[1], [2], [0]], True], "3-node cycle (strongly connected)"),
        # Example not strongly connected
        ([[[1], [2], []], False], "3-node path (not strongly connected)"),
        # Single node
        ([[[]], True], "Single node (trivially strongly connected)"),
        # Two nodes, strongly connected
        ([[[1], [0]], True], "2 nodes with bidirectional edges"),
        # Two nodes, not strongly connected
        ([[[1], []], False], "2 nodes, one-way edge"),
        # Cycle of 4 nodes
        ([[[1], [2], [3], [0]], True], "4-node cycle"),
        # Almost cycle of 4 nodes, missing one edge
        ([[[1], [2], [3], []], False], "4-node chain, missing back edge"),
        # Complete graph
        ([[[1, 2], [0, 2], [0, 1]], True], "Complete 3-node graph"),
    ]

    passed = 0
    print("Running strongly_connected() Tests...\n")

    for idx, (test, desc) in enumerate(tests):
        graph, want = test
        got = strongly_connected(graph)
        ok = got == want

        status = "✅ PASSED" if ok else "❌ FAILED"
        color = Colors.GREEN if ok else Colors.RED

        print(f"Test {idx + 1}: {color}{status}{Colors.END}")
        print(f"  Description     : {desc}")
        print(f"  Graph           : {graph}")
        print(f"  Expected output : {want}")
        print(f"  Actual output   : {got}")
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
