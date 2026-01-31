"""
The taxicab distance between two cells (r1, c1) and (r2, c2) in a grid is defined as abs(r1 - r2) + abs(c1 - c2).

You are given a grid of characters, screen, representing a screen with rows x cols pixels, where each element is one of 'R', 'G', or 'B'.

Return a grid, output, with the same dimensions, where:

    If screen[i][j] = 'R', output[i][j] is the taxicab distance from screen[i][j] to the closest 'G'
    If screen[i][j] = 'G', output[i][j] is the taxicab distance from screen[i][j] to the closest 'B'
    If screen[i][j] = 'B', output[i][j] is the taxicab distance from screen[i][j] to the closest 'R'

It is guaranteed that the screen contains at least one 'R', one 'G', and one 'B'.

Example 1:
screen = [
  "RRRGRB",
  "BGRGRR",
  "RRRGRR",
  "RGRRRR",
  "GBGRGG"
]

Output: [
  [2, 1, 1, 2, 1, 1],
  [1, 1, 1, 3, 1, 2],
  [2, 1, 1, 4, 1, 2],
  [1, 1, 1, 1, 1, 1],
  [1, 2, 1, 1, 3, 4]
]

Example 2:
screen = [
  "RGB"
]

Output: [
  [1, 1, 2]
]

Constraints:

    1 <= rows, cols <= 1000
    screen[i][j] is one of 'R', 'G', or 'B'
    screen contains at least one of each color
    All the rows have the same length
"""

from collections import deque


def multisource_bfs(screen, sources):

    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    rows, cols = len(screen), len(screen[0])
    distances = [[-1] * cols for _ in range(rows)]
    Q = deque()
    for r, c in sources:
        Q.append((r, c))
        distances[r][c] = 0

    while Q:
        r, c = Q.popleft()
        for dir_r, dir_c in directions:
            new_r = r + dir_r
            new_c = c + dir_c

            if (
                0 <= new_r < rows
                and 0 <= new_c < cols
                and distances[new_r][new_c] == -1
            ):
                distances[new_r][new_c] = distances[r][c] + 1
                Q.append((new_r, new_c))

    return distances


def get_sources(screen, target):
    rows, cols = len(screen), len(screen[0])
    sources = []

    for r in range(rows):
        for c in range(cols):
            if screen[r][c] == target:
                sources.append((r, c))

    return sources


def rgb_distances(screen):
    rows, cols = len(screen), len(screen[0])
    output = [[0] * cols for _ in range(rows)]

    targets = {"R": "G", "G": "B", "B": "R"}

    for color, target in targets.items():
        sources = get_sources(screen, target)
        distances = multisource_bfs(screen, sources)

        for r in range(rows):
            for c in range(cols):
                if screen[r][c] == color:
                    output[r][c] = distances[r][c]

    return output


def print_grid(grid):
    """Pretty print for 2D list (numbers) or list of strings (letters)"""
    if isinstance(grid[0], list):  # numeric grid
        return "\n".join(" ".join(f"{x:2}" for x in row) for row in grid)
    else:  # string rows
        return "\n".join(" ".join(row) for row in grid)


def run_tests():
    tests = [
        # Example from the book
        (
            ["RRRGRB", "BGRGRR", "RRRGRR", "RGRRRR", "GBGRGG"],
            [
                [2, 1, 1, 2, 1, 1],
                [1, 1, 1, 3, 1, 2],
                [2, 1, 1, 4, 1, 2],
                [1, 1, 1, 1, 1, 1],
                [1, 2, 1, 1, 3, 4],
            ],
        ),
        # Single row
        (["RGB"], [[1, 1, 2]]),
        # Single column
        (["R", "G", "B"], [[1], [1], [2]]),
        # All colors adjacent
        (["RGB", "BGR"], [[1, 1, 1], [1, 1, 1]]),
    ]

    passed, failed = 0, 0
    for i, (screen, want) in enumerate(tests, 1):
        got = rgb_distances(screen)

        print(f"Test {i}:")
        print(print_grid(screen))  # show screen grid
        if got == want:
            print("  ✅ PASSED")
            passed += 1
        else:
            print("  ❌ FAILED")
            print("  Expected:\n" + print_grid(want))
            print("  Got:\n" + print_grid(got))
            failed += 1
        print("-" * 50)

    print("SUMMARY")
    print(f"  Total: {len(tests)} | ✅ Passed: {passed} | ❌ Failed: {failed}")


run_tests()
