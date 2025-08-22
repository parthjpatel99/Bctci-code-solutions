"""
def is_tree(graph):
    edges = 0

    for node in range(len(graph)):
        edges += len(graph[node])
    edges = edges // 2
    if edges != len(graph) - 1:
        return False

    visited = set()

    def dfs(node):
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                dfs(nbr)

    dfs(0)

    if len(visited) == len(graph):
        return True
    return False
"""


def is_tree(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if not dfs(nei, node):
                    return False
            elif nei != parent:
                # Found a back edge → cycle
                return False
        return True

    # Graph must be connected and acyclic
    return dfs(0, -1) and len(visited) == len(graph)


def run_tests():
    class Colors:
        GREEN = "\033[92m"
        RED = "\033[91m"
        END = "\033[0m"

    tests = [
        ([[[1, 2], [0, 3, 4], [0], [1], [1]], True, "Example tree"]),
        ([[[1], [2], [3], [1]], False, "Has a cycle (not a tree)"]),
        ([[[]], True, "Single node"]),
        ([[[1], [0]], True, "Two nodes connected"]),
        ([[[], []], False, "Two nodes disconnected"]),
        ([[[1], [0, 2], [1, 3], [2]], True, "Line graph (valid tree)"]),
        ([[[1, 3], [2, 0], [3, 1], [0, 2]], False, "Cycle (not a tree)"]),
        (
            [
                [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]],
                False,
                "Complete graph K4 (not a tree)",
            ]
        ),
        ([[[1, 2, 3, 4], [0], [0], [0], [0]], True, "Star graph (valid tree)"]),
    ]

    passed = 0
    print("Running is_tree() Tests...\n")

    for idx, (graph, want, desc) in enumerate(tests):
        got = is_tree(graph)
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
