def race_overtaking(p1, p2):
    def isBefore(i):
        return p1[i] > p2[i]

    l = 0
    r = len(p1) - 1

    while r - l > 1:
        mid = (l + r) // 2

        if isBefore(mid):
            l = mid
        else:
            r = mid

    if p1[r] < p2[r]:
        return r


def run_tests():
    tests = [
        # Example 1 from book
        ([2, 4, 6, 8, 10], [1, 3, 5, 9, 11], 3),
        # Example
        ([2, 3, 4, 5, 6], [1, 2, 3, 6, 7], 3),
        # Example
        ([3, 4, 5], [2, 5, 6], 1),
        # Edge case - overtake at start
        ([2, 3], [1, 4], 1),
    ]

    total_tests = len(tests)
    passed_tests = 0
    failed_tests = 0

    print("==== Running Race Overtaking Tests ====\n")

    for i, (p1, p2, want) in enumerate(tests, 1):
        try:
            got = race_overtaking(p1, p2)

            if got == want:
                result = "✅ PASS"
                passed_tests += 1
            else:
                result = "❌ FAIL"
                failed_tests += 1

            print(f"Test #{i}: {result}")
            print(f"  Player 1 Positions: {p1}")
            print(f"  Player 2 Positions: {p2}")
            print(f"  Expected Overtakes: {want}")
            print(f"  Actual Overtakes: {got}")
            print("")

        except Exception as e:
            failed_tests += 1
            print(f"Test #{i}: ❌ ERROR")
            print(f"  Player 1 Positions: {p1}")
            print(f"  Player 2 Positions: {p2}")
            print(f"  Expected Overtakes: {want}")
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
