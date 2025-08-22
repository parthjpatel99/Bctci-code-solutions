def highest_average_elevation_gain(V, edges):
    graph = [[] for _ in range(V)]

    for node1, node2, elev in edges:
        graph[node1].append((node2, elev))
        graph[node2].append((node1, elev))

    visited = set()
    max_H = 0.0

    def dfs(node, connected_comp):
        visited.add(node)
        connected_comp.append(node)

        for nbr, _ in graph[node]:
            if nbr not in visited:
                dfs(nbr, connected_comp)

    for node in range(V):
        if node not in visited:
            connected_comp = []
            dfs(node, connected_comp)

            elevSum = 0.0
            edges = 0

            for u in connected_comp:
                for v, elev in graph[u]:
                    if v > u:
                        elevSum += elev
                        edges += 1
            if edges != 0:
                avg_cc_elev = elevSum // edges
            else:
                avg_cc_elev = 0
            max_H = max(max_H, avg_cc_elev)
    return max_H


def run_tests():
    tests = [
        # Example from the book
        (4, [[0, 1, 3], [1, 2, 2], [2, 3, 1], [3, 0, 2]], 2),  # V  # edges  # want
        # Single edge
        (2, [[0, 1, 5]], 5),
        # No edges
        (3, [], 0),
        # Multiple components
        (
            6,
            [
                [0, 1, 1],
                [1, 2, 2],  # Component 1: avg 1.5
                [3, 4, 3],
                [4, 5, 5],
            ],  # Component 2: avg 4.0
            4,
        ),
        # Single node component
        (3, [[0, 1, 2]], 2),  # Node 2 is isolated
    ]

    passed, failed = 0, 0
    for i, (V, edges, want) in enumerate(tests, 1):
        got = highest_average_elevation_gain(V, edges)
        if abs(got - want) < 1e-6:
            print(f"Test {i}: ✅ PASSED")
            passed += 1
        else:
            print(f"Test {i}: ❌ FAILED")
            print(f"  Input V: {V}")
            print(f"  Input edges: {edges}")
            print(f"  Expected: {want}")
            print(f"  Got: {got}")
            failed += 1
        print("-" * 50)

    print("SUMMARY")
    print(f"  Total: {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")


run_tests()
