"""
You are given the adjacency list of an undirected graph, graph, a node index, start, and an array, queries, where each element is a node index.

Return an array with the same length as queries, where the i-th element is an array with the shortest path from start to queries[i].

If there is no path from start to queries[i], return an empty array for the i-th element.

Example 1:
graph = [
   [1],           # Node 0
   [0, 2, 5, 4],  # Node 1
   [1, 4, 5],     # Node 2
   [],            # Node 3
   [5, 2, 1],     # Node 4
   [1, 2, 4]      # Node 5
]
start = 0
queries = [1, 0, 3, 4]

Output: [[0, 1], [0], [], [0, 1, 4]]
Node 3 cannot be reached from node 0

Example 2:
graph = [
   [1],           # Node 0
   [0, 2],        # Node 1
   [1]            # Node 2
]
start = 0
queries = [1, 2]

Output: [[0, 1], [0, 1, 2]]

Example 3:
graph = [
   [1],           # Node 0
   [0],           # Node 1
   [3],           # Node 2
   [2]            # Node 3
]
start = 0
queries = [1, 2, 3]

Output: [[0, 1], [], []]
Can only reach node 1 from node 0

Graph from example 1:
Shortest Path Queries

Constraints:

    graph.length <= 10^4
    graph[i].length < 10^4
    0 <= graph[i][j] < graph.length
    0 <= start < graph.length
    queries.length <= 10^3
    0 <= queries[i] < graph.length
    The graph is well-formed, with no parallel edges or self-loops
"""

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
