"""
In this classic problem, you are given a binary grid, grid, where 0 represents water and 1 represents solid ground. The goal is to count the number of islands in the grid, where an island is a four-directionally contiguous land region.

Return the number of islands in the grid.

Example 1: grid = [
  [0, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 0, 1, 1]
]
Output: 3

Example 2: grid = [
  []
]
Output: 0

Example 3: grid = [
  [1]
]
Output: 1

Example 4: grid = [
  [1, 0, 1],
  [0, 0, 0],
  [1, 0, 1]
]
Output: 4

Constraints:

    0 <= grid.length <= 1000
    0 <= grid[i].length <= 1000
    grid[i][j] is either 0 or 1
    All the rows have the same length
    Each island contains at most 500 cells
"""


def count_islands(grid):

    def dfs(visited, r, c):
        def isValid(r, c):
            return (
                0 <= r < len(grid)
                and 0 <= c < len(grid[0])
                and grid[r][c] == 1
                and (r, c) not in visited
            )

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for dir_r, dir_c in directions:
            new_r = r + dir_r
            new_c = c + dir_c
            if isValid(new_r, new_c):
                visited.add((new_r, new_c))
                dfs(visited, new_r, new_c)

    visited = set()
    res = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in visited and grid[r][c] == 1:
                visited.add((r, c))
                dfs(visited, r, c)
                res += 1

    return res


def run_tests():
    tests = [
        # Example 1 from the book
        ("Example 1", [[0, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 1]], 3),
        # Example 2 from the book
        ("Example 2", [[]], 0),
        # Edge case - single cell
        ("Single cell land", [[1]], 1),
        # Edge case - all water
        ("All water", [[0, 0], [0, 0]], 0),
        # Edge case - all land
        ("All land", [[1, 1], [1, 1]], 1),
        # Multiple islands
        ("Multiple islands", [[1, 0, 1], [0, 0, 0], [1, 0, 1]], 4),
    ]

    passed, failed = 0, 0

    for i, (desc, grid, want) in enumerate(tests, 1):
        print(f"Test {i}: {desc}")

        got = count_islands(grid)
        if got == want:
            print(f"  ✅ PASSED")
            passed += 1
        else:
            print(f"  ❌ FAILED")
            print(f"    Input Grid: {grid}")
            print(f"    Expected: {want}")
            print(f"    Got: {got}")
            failed += 1
        print("-" * 60)

    print("SUMMARY")
    print(f"  Total Tests: {len(tests)}")
    print(f"  ✅ Passed: {passed}")
    print(f"  ❌ Failed: {failed}")


run_tests()
