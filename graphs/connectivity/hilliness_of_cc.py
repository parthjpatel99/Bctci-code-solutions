"""
We're given the adjacency list, graph, of a non-empty, undirected graph with V nodes and an array, heights, of length V, where heights[i] is a floating-point number representing the height of node i.

A connected component is a maximal set of nodes such that there is a path between any two nodes in the set.

The elevation gain of an edge is the absolute difference of the heights of its endpoints. The hilliness of a connected component is the average elevation gain of the edges in it, or 0 if it has a single node. The hilliest connected component is the one with maximum hilliness.

Find the hilliest connected component and return its hilliness.

Example 1:
graph = [
   [1, 3],       # Node 0
   [0, 2],       # Node 1
   [1, 3],       # Node 2
   [0, 2]        # Node 3
]
heights = [4.0, 1.0, 3.0, 2.0]

Output: 2.0
The graph has a single connected component
The edge elevation gains are:
- |4 - 1| = 3 for [0, 1]
- |1 - 3| = 2 for [1, 2]
- |3 - 2| = 1 for [2, 3]
- |2 - 4| = 2 for [3, 0]
The average is 2

Example 2:
graph = [
   []           # Node 0
]
heights = [5.0]

Output: 0.0
A single-node connected component has hilliness 0

Example 3:
graph = [
   [1],          # Node 0
   [0],          # Node 1
   [3],          # Node 2
   [2]           # Node 3
]
heights = [1.5, 5.5, 0.0, 5.0]

Output: 5.0
The graph has two components:
- {0, 1}, with a single edge with elevation gain 4.0
- {2, 3}, with a single edge with elevation gain 5.0

Example 4:
graph = [
   [1, 2],       # Node 0
   [0, 2],       # Node 1
   [0, 1]        # Node 2
]
heights = [3.0, 3.0, 3.0]
Output: 0.0
When all nodes have the same height, the elevation gain is 0 for all edges

Example 1:
Hilliest connected component 1

Constraints:

    1 ≤ graph.length ≤ 1000
    graph[i].length < 1000
    0 ≤ graph[i][j] < graph.length
    The adjacency list is properly formatted, with no parallel edges or self-loops
    heights.length = graph.length
    0 ≤ heights[i] < 10^9
    heights[i] is a floating-point number
"""


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
