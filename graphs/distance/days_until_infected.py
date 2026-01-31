"""
Some computers in a network have been infected by a virus. We are given the adjacency list of an undirected, connected graph, graph, representing the computer network, and an array, infected, with the indices of the infected nodes.

Every day, the virus spreads to all computers directly connected to an infected neighbor computer.

How many days will it take to infect all computers?

For example, for this graph:
Days until all infected

It takes 3 days for the virus to infect all computers.

Example 1:
graph = [
  [1, 2],       # Node 0
  [0, 2],       # Node 1
  [0, 1, 3],    # Node 2
  [2]           # Node 3
]
infected = [0]

Output: 2
On day 1, nodes 1 and 2 get infected
On day 2, node 3 gets infected

Example 2:
graph = [
  [1],          # Node 0
  [0, 2],       # Node 1
  [1, 3],       # Node 2
  [2, 4],       # Node 3
  [3],          # Node 4
]
infected = [0, 4]

Output: 2
The virus spreads through the line graph from both ends.

Example 3:
graph = [
  [1, 2],       # Node 0
  [0, 3],       # Node 1
  [0, 3],       # Node 2
  [1, 2],       # Node 3
]
infected = [0, 3]

Output: 1. With two initial infected nodes, all other nodes are infected after
one day.

Constraints:

    1 <= graph.length <= 10^4
    graph[i].length < 10^4
    0 <= graph[i][j] < graph.length
    1 <= infected.length <= graph.length
    0 <= infected[i] < graph.length
    infected does not contain duplicates
    The graph is well-formed, with no parallel edges or self-loops
    The graph is connected
"""

from collections import deque


def all_infected(graph, infected):

    Q = deque()
    distances = {}
    for node in infected:
        distances[node] = 0
        Q.append(node)
    while Q:
        node = Q.popleft()
        for nbr in graph[node]:
            if nbr not in distances:
                distances[nbr] = distances[node] + 1
                Q.append(nbr)

    if len(distances) < len(graph):
        return -1
    return max(distances.values())


def run_tests():
    tests = [
        # Example from the book
        (
            [
                [1, 14],
                [0, 2],
                [1, 3],
                [2, 4],
                [3, 5, 19],
                [4, 6],
                [5, 7],
                [6, 8],
                [7, 9, 21],
                [8, 10],
                [9, 11],
                [10, 12],
                [11, 13],
                [12, 14],
                [0, 13, 15],
                [14, 16],
                [15, 17],
                [16, 18, 20],
                [17, 19],
                [18, 4],
                [17, 21],
                [8, 20],
            ],
            [0, 8, 17],
            3,
        ),
        ([[1, 2], [0, 2], [0, 1, 3], [2]], [0], 2),  # graph  # infected  # want
        # Single node graph
        ([[]], [0], 0),
        # Line graph
        ([[1], [0, 2], [1, 3], [2]], [0], 3),
        # Multiple initial infected nodes
        ([[1, 2], [0, 3], [0, 3], [1, 2]], [0, 3], 1),
    ]

    total = len(tests)
    passed = 0

    print("\n===== Running Tests =====\n")

    for i, (graph, infected, want) in enumerate(tests, 1):
        got = all_infected(graph, infected)
        status = "✅ PASS" if got == want else "❌ FAIL"
        if got == want:
            passed += 1

        print(f"Test {i}: {status}")
        print(f"  Inputs:")
        print(f"    Graph: {graph}")
        print(f"    Infected: {infected}")
        print(f"  Expected: {want}")
        print(f"  Got:      {got}")
        print("-" * 40)

    print(f"\nSummary: {passed}/{total} tests passed.")


run_tests()
