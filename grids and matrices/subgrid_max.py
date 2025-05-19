def subgrid_maximums(grid):
    R = len(grid)
    C = len(grid[0])

    res = [row.copy() for row in grid]

    for r in range(R - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            if r + 1 < R:
                res[r][c] = max(res[r][c], res[r+1][c])
            if c + 1 < C:
                res[r][c] = max(res[r][c], res[r][c+1])
    
    return res

def run_tests():
    tests = [
        # Example from book
        ([[1, 5, 3],
          [4, -1, 0],
          [2, 0, 2]],
         [[5, 5, 3],
          [4, 2, 2],
          [2, 2, 2]]),
        # Edge case - 1x1 grid
        ([[5]], [[5]]),
        # Edge case - single row
        ([[1, 2, 3]], [[3, 3, 3]]),
        # Edge case - single column
        ([[1], [2], [3]], [[3], [3], [3]]),
        # Edge case - negative numbers
        ([[-1, -2],
          [-3, -4]],
         [[-1, -2],
          [-3, -4]]),
    ]

    for i, (grid, want) in enumerate(tests, 1):
        got = subgrid_maximums(grid)
        status = "✅" if got == want else "❌"
        print(f"Test {i}: {status}")
        print("Inputs:")
        for row in grid:
            print(row)
        print("Expected Output:")
        for row in want:
            print(row)
        print("Actual Output:")
        for row in got:
            print(row)
        print("-" * 40)

run_tests()