from collections import deque


def shortest_path_queries(graph, start, queries):
    queue = deque()
    queue.append(start)
    predecessors = {start: None}

    while queue:
        node = queue.popleft()
        for nbr in graph[node]:
            if nbr not in predecessors:
                predecessors[nbr] = node
                queue.append(nbr)

    res = []
    for node in queries:
        if node not in predecessors:
            res.append([])
        else:
            path = [node]
            while path[-1] != start:
                path.append(predecessors[path[-1]])
            path.reverse()
            res.append(path)

    return res


def run_tests():
    tests = [
        # Format: (graph, start, queries, expected)
        # Example
        (
            [[1], [0, 2, 5, 4], [1, 4, 5], [], [5, 2, 1], [1, 2, 4]],
            0,
            [1, 0, 3, 4],
            [[0, 1], [0], [], [0, 1, 4]],
            "Example case",
        ),
        # Simple line graph
        ([[1], [0, 2], [1]], 0, [1, 2], [[0, 1], [0, 1, 2]], "Simple line"),
        # Disconnected components
        (
            [[1], [0], [3], [2]],
            0,
            [1, 2, 3],
            [[0, 1], [], []],
            "Disconnected components",
        ),
        # Complete graph
        ([[1, 2], [0, 2], [0, 1]], 0, [1, 2], [[0, 1], [0, 2]], "Complete graph"),
        # Single node
        ([[]], 0, [0], [[0]], "Single node"),
        # Empty queries
        ([[1], [0]], 0, [], [], "Empty queries"),
    ]

    passed, failed = 0, 0

    for i, (graph, start, queries, want, desc) in enumerate(tests, 1):
        got = shortest_path_queries(graph, start, queries)
        if got == want:
            print(f"✅ Test {i}: {desc} PASSED")
            passed += 1
        else:
            print(f"❌ Test {i}: {desc} FAILED")
            print(f"    Inputs: graph={graph}, start={start}, queries={queries}")
            print(f"    Expected: {want}")
            print(f"    Got:      {got}")
            failed += 1
        print("-" * 50)

    print("SUMMARY")
    print(f"  ✅ Passed: {passed}")
    print(f"  ❌ Failed: {failed}")
    print(f"  Total: {len(tests)}")


run_tests()
