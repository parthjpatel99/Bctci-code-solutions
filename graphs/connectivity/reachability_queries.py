"""
def connected_component_queries(graph, queries):
    res = []
    visited = set()

    def dfs(node):
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                dfs(nbr)

    for query in queries:
        dfs(query[0])
        if query[1] not in visited:
            res.append(False)
        else:
            res.append(True)
        visited.clear()

    return res
"""


def connected_component_queries(graph, queries):
    node_to_cc = {}

    def dfs(node, cc_id):
        if node in node_to_cc:
            return
        node_to_cc[node] = cc_id
        for nbr in graph[node]:
            dfs(nbr, cc_id)

    cc_id = 0
    for node in range(len(graph)):
        if node not in node_to_cc:
            dfs(node, cc_id)
            cc_id += 1

    res = []

    for node1, node2 in queries:
        res.append(node_to_cc[node1] == node_to_cc[node2])

    return res


def run_tests():
    class Colors:
        GREEN = "\033[92m"
        RED = "\033[91m"
        END = "\033[0m"

    tests = [
        # Cycle graph with 6 nodes
        (
            [
                [[1, 5], [0, 2, 4], [1, 3, 5], [2, 4], [1, 3, 5], [0, 2, 4]],
                [(0, 4), (0, 3)],
                [True, True],
            ],
            "Cycle graph with 6 nodes",
        ),
        # Example from book
        (
            [
                [[1], [0, 2, 5, 4], [1, 4, 5], [], [5, 2, 1], [1, 2, 4]],
                [(0, 4), (0, 3)],
                [True, False],
            ],
            "Book example",
        ),
        # Simple line graph
        ([[[1], [0, 2], [1]], [(0, 2), (0, 1)], [True, True]], "Line graph"),
        # Disconnected components
        (
            [[[1], [0], [3], [2]], [(0, 1), (0, 2), (2, 3)], [True, False, True]],
            "Disconnected graph",
        ),
        # Complete graph
        (
            [[[1, 2], [0, 2], [0, 1]], [(0, 1), (1, 2), (0, 2)], [True, True, True]],
            "Complete graph",
        ),
        # Single node
        ([[[]], [(0, 0)], [True]], "Single node graph"),
        # Empty queries
        ([[[1], [0]], [], []], "Empty queries"),
    ]

    passed = 0
    print("Running connected_component_queries() Tests...\n")

    for idx, (test, desc) in enumerate(tests):
        graph, queries, want = test
        got = connected_component_queries(graph, queries)
        ok = got == want

        status = "✅ PASSED" if ok else "❌ FAILED"
        color = Colors.GREEN if ok else Colors.RED

        print(f"Test {idx + 1}: {color}{status}{Colors.END}")
        print(f"  Description     : {desc}")
        print(f"  Graph           : {graph}")
        print(f"  Queries         : {queries}")
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
