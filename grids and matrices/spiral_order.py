def spiral(n):
    res = [[0] * n for _ in range(n)]
    val = n * n - 1

    def isValid(grid, r, c):
        return 0 <= r < n and 0 <= c < n and grid[r][c] == 0

    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    r = n - 1
    c = n - 1
    dir = 0
    while val > 0:
        res[r][c] = val
        val -= 1

        if not isValid(res, r + directions[dir][0], c + directions[dir][1]):
            dir = (dir + 1) % 4

        r = r + directions[dir][0]
        c = c + directions[dir][1]

    return res


def run_tests():
    tests = [
        # Example from book
        (
            5,
            [
                [16, 17, 18, 19, 20],
                [15, 4, 5, 6, 21],
                [14, 3, 0, 7, 22],
                [13, 2, 1, 8, 23],
                [12, 11, 10, 9, 24],
            ],
        ),
        # Edge case - 1x1
        (1, [[0]]),
        # Edge case - 3x3
        (3, [[4, 5, 6], [3, 0, 7], [2, 1, 8]]),
    ]

    passed_count = 0

    for i, (n, want) in enumerate(tests):
        got = spiral(n)
        passed = got == want
        if passed:
            passed_count += 1
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"Test {i + 1}: {status}")
        print(f"  Input n: {n}")
        print(f"  Expected Output: {want}")
        print(f"  Actual Output:   {got}")
        print()

    total_tests = len(tests)
    failed_count = total_tests - passed_count
    print("====== SUMMARY ======")
    print(f"Total tests run: {total_tests}")
    print(f"✅ Passed: {passed_count}")
    print(f"❌ Failed: {failed_count}")


run_tests()