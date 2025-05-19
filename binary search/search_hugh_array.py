def find_through_api(target, fetch):
    def isBefore(i):
        return fetch(i) < target

    l = 0
    r = 1
    if fetch(l) == target:
        return l
    while fetch(r) != -1:
        r = r * 2

    while r - l > 1:
        mid = (l + r) // 2
        if isBefore(mid):
            l = mid
        else:
            r = mid

    if fetch(r) == target:
        return r
    return -1


def run_tests():
    def make_fetch_function(secret_array):
        def fetch(idx):
            if idx >= len(secret_array) or idx < 0:
                return -1
            return secret_array[idx]

        return fetch

    tests = [
        # Example 1 - target exists
        (5, 2, [1, 3, 5, 7, 9]),
        # Example 2 - target doesn't exist
        (6, -1, [1, 3, 5, 7, 9]),
        # Edge case - target at start
        (1, 0, [1, 3, 5, 7, 9]),
        # Edge case - target at end
        (9, 4, [1, 3, 5, 7, 9]),
        # All duplicates
        (1, 0, [1, 1, 1, 1, 1, 1, 1, 1]),
    ]

    total_tests = len(tests)
    passed_tests = 0
    failed_tests = 0

    print("==== Running API Search Tests ====\n")

    for i, (target, want, secret_array) in enumerate(tests, 1):
        try:
            fetch = make_fetch_function(secret_array)
            got = find_through_api(target, fetch)

            if got == want:
                result = "✅ PASS"
                passed_tests += 1
            else:
                result = "❌ FAIL"
                failed_tests += 1

            print(f"Test #{i}: {result}")
            print(f"  Secret Array: {secret_array}")
            print(f"  Target: {target}")
            print(f"  Expected Index: {want}")
            print(f"  Actual Index: {got}")
            print("")

        except Exception as e:
            failed_tests += 1
            print(f"Test #{i}: ❌ ERROR")
            print(f"  Secret Array: {secret_array}")
            print(f"  Target: {target}")
            print(f"  Expected Index: {want}")
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
