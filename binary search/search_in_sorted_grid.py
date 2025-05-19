def search_in_sorted_grid(grid, target):
    if not grid:
        return [-1, -1]
    rows = len(grid)
    cols = len(grid[0])

    def isBefore(i):
        row = i // cols
        col = i % cols

        return grid[row][col] < target

    l = 0
    r = rows * cols - 1

    while r - l > 1:
        mid = (r + l) // 2
        if isBefore(mid):
            l = mid
        else:
            r = mid

    row = r // cols
    col = r % cols

    if grid[row][col] == target:
        return [row, col]
    else:
        return [-1, -1]


def run_tests():
    tests = [
        # Example 1
        ([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 9, [1, 1]),
        # Example 2
        ([[1, 3, 5], [7, 9, 11]], 4, [-1, -1]),
        # Edge case - empty grid
        ([], 1, [-1, -1]),
        # Edge case - target at start
        ([[1]], 1, [0, 0]),
        # Edge case - target at end
        ([[1, 2], [3, 4]], 4, [1, 1]),
    ]

    total_tests = len(tests)
    passed_tests = 0
    failed_tests = 0

    print("==== Running Grid Search Tests ====\n")

    for i, (grid, target, want) in enumerate(tests, 1):
        try:
            got = search_in_sorted_grid(grid, target)

            if got == want:
                result = "✅ PASS"
                passed_tests += 1
            else:
                result = "❌ FAIL"
                failed_tests += 1

            print(f"Test #{i}: {result}")
            print(f"  Grid: {grid}")
            print(f"  Target: {target}")
            print(f"  Expected Position: {want}")
            print(f"  Actual Position: {got}")
            print("")

        except Exception as e:
            failed_tests += 1
            print(f"Test #{i}: ❌ ERROR")
            print(f"  Grid: {grid}")
            print(f"  Target: {target}")
            print(f"  Expected Position: {want}")
            print(f"  Error: {str(e)}")
            print("")

    # Print summary
    print("==== Test Summary ====")
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed_tests} ({passed_tests/total_tests*100:.1f}%)")
    print(f"Failed: {failed_tests} ({failed_tests/total_tests*100:.1f}%)")

    if failed_tests == 0:
        print("\n✅ All tests passed!")
    else:
        print(f"\n❌ {failed_tests} test(s) failed!")


run_tests()
