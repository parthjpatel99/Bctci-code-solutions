"""We are given an array, furniture, where each element consists of four integer coordinates, [x_min, y_min, x_max, y_max], indicating the boundary of a rectangular piece of furniture. The furniture pieces are non-overlapping (they can share an edge or a corner).

We are playing the game 'the floor is lava,' where we have to reach from the first piece of furniture (the one at index 0 in furniture) to the last one without touching the floor, only jumping on furniture. If we can jump at most a distance of d, where d is an integer, can we win?

Recall that:

distance((x1, y1), (x2, y2)) = sqrt((x1 - x2)^2 + (y1 - y2)^2).

For example, if this is the furniture and d is 5, we can jump from the furniture labeled 0 to the one labeled 4 with the indicated jumps:
The floor is lava

However, if d is 4 for the same furniture, we can't do it.

Example 1:
furniture = [
  [1, 1, 9, 5],
  [12, 9, 20, 13],
  [16, 2, 22, 7],
  [24, 9, 26, 11],
  [29, 1, 31, 5]
]
d = 5

Output: True
See the image above

Example 2:
furniture = [
  [1, 1, 9, 5],
  [12, 9, 20, 13],
  [16, 2, 22, 7],
  [24, 9, 26, 11],
  [29, 1, 31, 5]
]
d = 4
Output: False
See the image above

Constraints:

    1 <= furniture.length <= 1000
    furniture[i] is a list of 4 integers
    0 <= furniture[i][0] < furniture[i][2] < 10^9
    0 <= furniture[i][1] < furniture[i][3] < 10^9
    The furniture pieces are non-overlapping
    0 < d <= 10^9
    All coordinates and distances are floating-point numbers
"""

import math


def segment(min1, max1, min2, max2):
    return max(0, max(min1, min2) - min(max1, max2))


def distance(furniture1, furniture2):
    x_min1, y_min1, x_max1, y_max1 = furniture1
    x_min2, y_min2, x_max2, y_max2 = furniture2

    x_gap = segment(x_min1, x_max1, x_min2, x_max2)
    y_gap = segment(y_min1, y_max1, y_min2, y_max2)

    if x_gap == 0:
        return y_gap
    elif y_gap == 0:
        return x_gap
    else:
        return math.sqrt(x_gap**2 + y_gap**2)


def can_reach(furniture, d):
    V = len(furniture)
    graph = [[] for _ in range(V)]

    for i in range(V):
        for j in range(i + 1, V):
            if distance(furniture[i], furniture[j]) <= d:
                graph[i].append(j)
                graph[j].append(i)

    visited = {0}

    def visit(node):
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                visit(nbr)

    visit(0)

    return V - 1 in visited


def run_tests():
    tests = [
        # Example 1 from the book:
        (
            [
                [
                    [1, 1, 9, 5],
                    [12, 9, 20, 13],
                    [16, 2, 22, 7],
                    [24, 9, 26, 11],
                    [29, 1, 31, 5],
                ],
                5,
                True,
            ]
        ),
        # Example 2 from the book:
        (
            [
                [
                    [1, 1, 9, 5],
                    [12, 9, 20, 13],
                    [16, 2, 22, 7],
                    [24, 9, 26, 11],
                    [29, 1, 31, 5],
                ],
                4,
                False,
            ]
        ),
        (
            [
                [[0, 0, 1, 1], [1, 1, 2, 2], [2, 2, 3, 3], [3, 3, 4, 4], [4, 4, 5, 5]],
                0,
                True,
            ]
        ),
        (
            [
                [[0, 0, 1, 1], [1, 1, 2, 2], [2, 2, 3, 3], [3, 3, 4, 4], [4, 4, 5, 5]],
                1,
                True,
            ]
        ),
        ([[[0, 0, 1, 1], [1, 1, 2, 2], [3, 3, 4, 4], [4, 4, 5, 5]], 1, False]),
        ([[[0, 0, 1, 1], [1, 1, 2, 2], [3, 3, 4, 4], [4, 4, 5, 5]], 2, True]),
        ([[[0, 0, 1, 1]], 5, True]),
        ([[[0, 0, 1, 1], [10, 10, 11, 11]], 5, False]),
        ([[[0, 0, 1, 1], [5, 5, 6, 6]], 5.7, True]),
        ([[[0, 0, 1, 1], [5, 5, 6, 6]], 5.6, False]),
        ([[[0, 0, 1, 1], [1, 0, 2, 1], [2, 0, 3, 1]], 1.5, True]),
    ]

    passed = 0

    print("\n===== Running Tests =====\n")

    for idx, (furniture, d, want) in enumerate(tests, start=1):
        got = can_reach(furniture, d)
        ok = got == want

        print(f"Test {idx}: {'✅ PASSED' if ok else '❌ FAILED'}")
        print(f"  • Input furniture: {furniture}")
        print(f"  • Input distance d: {d}")
        print(f"  • Expected: {want}")
        print(f"  • Got:      {got}")
        print()

        if ok:
            passed += 1

    total = len(tests)
    print("===== Summary =====")
    print(f"Passed: {passed}/{total} tests ({passed/total*100:.1f}%)")


run_tests()
