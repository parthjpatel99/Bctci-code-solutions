"""
Given the adjacency list of an undirected graph, graph, and two distinct nodes, node1 and node2, return a simple path from node1 to node2.

A simple path does not repeat any nodes. Return an empty array if there is no path from node1 to node2.

Example 1:
graph = [
  [1],
  [0, 2, 5, 4],
  [1, 4, 5],
  [],
  [5, 2, 1],
  [1, 2, 4]
]
node1 = 0
node2 = 4

Output: [0, 1, 4]
There are other valid answers, like [0, 1, 2, 5, 4].

Example 2:
graph = [
  [1],
  [0, 2, 5, 4],
  [1, 4, 5],
  [],
  [5, 2, 1],
  [1, 2, 4]
]
node1 = 0
node2 = 3

Output: []
There is no path to node 3.

Example 3:
graph = [
  [1],
  [0, 2],
  [1]
]
node1 = 0
node2 = 2

Output: [0, 1, 2]
A simple path through all nodes.

Here is a drawing of the graph from Example 1:
Graph Path

Constraints:

    graph.length ≤ 1000
    graph[i].length < 1000
    0 ≤ graph[i][j] < graph.length
    0 ≤ node1, node2 < graph.length
    node1 != node2
    The adjacency list is properly formatted, with no parallel edges or self-loops

"""


def path(graph, node1, node2):
    path = []
    visited = set()

    def dfs(node):
        path.append(node)
        visited.add(node)
        if node == node2:
            return True
        for nbr in graph[node]:
            if nbr not in visited:
                if dfs(nbr):
                    return True
        path.pop()
        return False

    if dfs(node1):
        return path
    return []


def run_tests():
    class Colors:
        GREEN = "\033[92m"
        RED = "\033[91m"
        END = "\033[0m"

    tests = [
        # Example 1 from book - graph from Figure 8
        (
            [[[1], [0, 2, 5, 4], [1, 4, 5], [], [5, 2, 1], [1, 2, 4]], 0, 4, [0, 1, 4]],
            "Book Fig 8 - valid path",
        ),
        # Example 2 from book - no path exists
        (
            [[[1], [0, 2, 5, 4], [1, 4, 5], [], [5, 2, 1], [1, 2, 4]], 0, 3, []],
            "Book Fig 8 - no path",
        ),
        # Simple line graph
        ([[[1], [0, 2], [1]], 0, 2, [0, 1, 2]], "Simple line graph"),
        # Cycle graph
        ([[[1, 3], [0, 2], [1, 3], [0, 2]], 0, 2, [0, 1, 2]], "Cycle graph"),
        # Disconnected graph
        ([[[1], [0], [3], [2]], 0, 2, []], "Disconnected graph"),
        # Complete graph
        ([[[1, 2], [0, 2], [0, 1]], 0, 2, [0, 2]], "Complete graph"),
    ]

    passed = 0
    print("Running path() Tests...\n")

    for idx, (test, desc) in enumerate(tests):
        graph, node1, node2, want = test
        got = path(graph, node1, node2)
        ok = True

        if not want:
            if got:
                ok = False
        else:
            if not (got and got[0] == node1 and got[-1] == node2):
                ok = False
            else:
                # Verify path validity
                for i in range(len(got) - 1):
                    if got[i + 1] not in graph[got[i]]:
                        ok = False
                        break
                # Verify no duplicates
                if len(got) != len(set(got)):
                    ok = False

        status = "✅ PASSED" if ok else "❌ FAILED"
        color = Colors.GREEN if ok else Colors.RED
        print(f"Test {idx + 1}: {color}{status}{Colors.END}")
        print(f"  Description     : {desc}")
        print(f"  Start node      : {node1}")
        print(f"  End node        : {node2}")
        if want:
            print(f"  Expected output : {want} (or any valid path)")
        else:
            print(f"  Expected output : [] (no path)")
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
