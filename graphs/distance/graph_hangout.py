from collections import deque
import math


def walking_distance_to_coffee(graph, node1, node2, node3):

    def bfs(graph, start):
        queue = deque()
        distances = {start: 0}
        queue.append(start)

        while queue:
            node = queue.popleft()
            for nbr in graph[node]:
                if nbr not in distances:
                    distances[nbr] = distances[node] + 1
                    queue.append(nbr)

        return distances

    distance1 = bfs(graph, node1)
    distance2 = bfs(graph, node2)
    distance3 = bfs(graph, node3)

    res = math.inf
    for i in range(len(graph)):
        res = min(res, distance1[i] + distance2[i] + distance3[i])
    return res


def run_tests():
    tests = [
        # Format: (graph, node1, node2, node3, expected, description)
        (
            [
                [1, 14],  # 0: Outer ring connections
                [0, 2],  # 1
                [1, 3],  # 2
                [2, 4],  # 3
                [3, 5, 19],  # 4: Connector from outer to inner ring
                [4, 6],  # 5
                [5, 7],  # 6
                [6, 8],  # 7
                [7, 9, 21],  # 8: Connector from outer to inner ring
                [8, 10],  # 9
                [9, 11],  # 10
                [10, 12],  # 11
                [11, 13],  # 12
                [12, 14],  # 13
                [0, 13, 15],  # 14: Connector from outer to inner ring
                [14, 16],  # 15
                [15, 17],  # 16
                [16, 18, 20],  # 17: Center node connections
                [17, 19],  # 18
                [18, 4],  # 19
                [17, 21],  # 20
                [8, 20],  # 21
            ],
            14,
            4,
            8,
            9,
            "Complex ring graph",
        ),
        # Cycle with 5 nodes
        ([[1, 4], [0, 2], [1, 3], [2, 4], [0, 3]], 0, 2, 4, 3, "Cycle graph"),
        # Simple line graph
        ([[1], [0, 2], [1]], 0, 1, 2, 2, "Simple line"),
        # Star graph - optimal meeting point is center
        ([[1], [0, 2, 3, 4], [1], [1], [1]], 0, 2, 3, 3, "Star graph"),
        # Complete graph - any node works
        ([[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]], 0, 1, 2, 2, "Complete graph"),
        # Edge case - all start same
        ([[1], [0]], 0, 0, 0, 0, "All same node"),
        # Edge case - two same
        ([[1], [0, 2], [1]], 0, 0, 2, 2, "Two same node"),
    ]

    passed, failed = 0, 0

    for i, (graph, node1, node2, node3, want, desc) in enumerate(tests, 1):
        got = walking_distance_to_coffee(graph, node1, node2, node3)
        if got == want:
            print(f"✅ Test {i}: {desc} PASSED")
            passed += 1
        else:
            print(f"❌ Test {i}: {desc} FAILED")
            print(f"    Inputs: graph={graph}, nodes=({node1}, {node2}, {node3})")
            print(f"    Expected: {want}")
            print(f"    Got:      {got}")
            failed += 1
        print("-" * 50)

    print("SUMMARY")
    print(f"  ✅ Passed: {passed}")
    print(f"  ❌ Failed: {failed}")
    print(f"  Total: {len(tests)}")


run_tests()
