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
