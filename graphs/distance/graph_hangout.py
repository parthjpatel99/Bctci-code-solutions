"""
Three friends want to meet. They live in nodes in a connected, undirected graph.

You are given the adjacency list, graph, and the nodes where they start, node1, node2, and node3.

Return the minimum number of edges they need to traverse in total between the three to meet at any node in the graph.

For example, for this graph:
Graph Hangout

If the three friends start at the nodes labeled 1, 2 and 3, they can each get to the middle node by traversing 3 edges. The next closest meeting point is at one of the starting nodes, where the other two friends have to traverse 5 edges each. Thus, the answer is 9.

Example 1:
graph = [
    [1, 4],   # Node 0
    [0, 2],   # Node 1
    [1, 3],   # Node 2
    [2, 4],   # Node 3
    [0, 3]    # Node 4
]
node1 = 0
node2 = 2
node3 = 4

Output: 3
They can meet at node 0 or 4 in combined 3 steps

Example 2:
graph = [
    [1, 2, 3],  # Node 0
    [0, 2, 3],  # Node 1
    [0, 1, 3],  # Node 2
    [0, 1, 2]   # Node 3
]
node1 = 0
node2 = 1
node3 = 2

Output: 2
In a complete graph, they can meet at any node

Constraints:

    graph.length <= 10^4
    graph[i].length < 10^4
    0 <= graph[i][j] < graph.length
    0 <= node1, node2, node3 < graph.length
    The graph is well-formed, with no parallel edges or self-loops
"""

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
