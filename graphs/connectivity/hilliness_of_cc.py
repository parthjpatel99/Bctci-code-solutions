def max_hilliness(graph, heights):
    V = len(graph)
    visited = set()
    max_H = 0.0

    def dfs(node, connected_comp):
        visited.add(node)
        connected_comp.append(node)
        for nbr in graph[node]:
            if nbr not in visited:
                dfs(nbr, connected_comp)

    for node in range(V):
        if node not in visited:
            connected_comp = []
            dfs(node, connected_comp)

            edges = 0
            edgeSum = 0.0

            for u in connected_comp:
                for v in graph[u]:
                    if v > u:
                        edgeSum += abs(heights[u] - heights[v])
                        edges += 1

            if edges > 0:
                hilliness = edgeSum / edges
            else:
                hilliness = 0.0
            max_H = max(max_H, hilliness)

    return max_H


def run_tests():
    tests = [
        # Example
        [[[1, 3], [0, 2], [1, 3], [0, 2]], [4, 1, 3, 2], 2],
        # Single node component
        [[[]], [5], 0],
        # Two disconnected components
        [[[1], [0], [3], [2]], [1, 4, 2, 5], 3],
        # All nodes same height
        [[[1, 2], [0, 2], [0, 1]], [3, 3, 3], 0],
        # Line graph
        [[[1], [0, 2], [1]], [1, 5, 2], 3.5],
        # Complete graph
        [
            [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]],
            [1, 4, 7, 10],
            (3 + 6 + 9 + 3 + 6 + 3) / 6,
        ],
    ]

    passed, failed = 0, 0
    for i, (graph, heights, want) in enumerate(tests, 1):
        got = max_hilliness(graph, heights)
        if abs(got - want) < 0.0001:
            print(f"Test {i}: ✅ PASSED")
            passed += 1
        else:
            print(f"Test {i}: ❌ FAILED")
            print(f"  Input graph: {graph}")
            print(f"  Input heights: {heights}")
            print(f"  Expected: {want}")
            print(f"  Got: {got}")
            failed += 1
        print("-" * 50)

    print("SUMMARY")
    print(f"  Total: {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")


run_tests()
