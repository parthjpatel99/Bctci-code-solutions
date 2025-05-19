def target_count_divisible_by_k(arr, target, k):
    def bsearchfirst():
        def isBefore(i):
            return arr[i] < target

        l = 0
        r = len(arr) - 1

        if len(arr) == 0 or arr[l] > target or arr[r] < target:
            return -1
        if arr[l] == target:
            return l

        while r - l > 1:
            mid = (l + r) // 2

            if isBefore(mid):
                l = mid
            else:
                r = mid

        if arr[r] == target:
            return r
        return -1

    def bsearchsecond():
        def isBefore(i):
            return arr[i] <= target

        l = 0
        r = len(arr) - 1

        if len(arr) == 0 or arr[l] > target or arr[r] < target:
            return -1
        if arr[r] == target:
            return r

        while r - l > 1:
            mid = (l + r) // 2
            if isBefore(mid):
                l = mid
            else:
                r = mid

        if arr[l] == target:
            return l
        return -1

    first = bsearchfirst()
    second = bsearchsecond()
    print(f"First = {first}")
    print(f"Second = {second}")

    #Edge case: Element not present, 0 occurrence. 0 is multiple of any k
    if first == -1 and second == -1:
        return True

    if (second - first + 1) % k == 0:
        return True

    return False


def run_tests():
    tests = [
        # Example 1
        ([1, 2, 2, 2, 2, 2, 2, 3], 2, 3, True),
        # Example 2
        ([1, 2, 2, 2, 2, 2, 2, 3], 2, 4, False),
        # Example 3: 0 occurrences, 0 is multiple of any number
        ([1, 2, 2, 2, 2, 2, 2, 3], 4, 3, True),
        # Example 4
        ([1, 1, 2, 2, 2], 1, 3, False),
        # Edge case - empty array
        ([], 1, 2, True),
        # single occurrence, at the start
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 1, 1, True),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 1, 2, False),
        # single occurrence, at the end
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 19, 1, True),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 19, 2, False),
        # single occurrence, in the middle
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 9, 1, True),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 9, 2, False),
        # smaller than any elements
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 0, 1, True),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 0, 2, True),
        # larger than any elements
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 20, 1, True),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 20, 2, True),
        # Edge case - every occurrence is target
        ([5, 5, 5, 5, 5], 5, 5, True),
        ([5, 5, 5, 5, 5], 5, 3, False),
    ]

    total_tests = len(tests)
    passed_tests = 0
    failed_tests = 0

    print("==== Running Tests ====\n")

    for i, (arr, target, k, expected) in enumerate(tests, 1):
        try:
            actual = target_count_divisible_by_k(arr, target, k)

            if actual == expected:
                result = "✅ PASS"
                passed_tests += 1
            else:
                result = "❌ FAIL"
                failed_tests += 1

            print(f"Test #{i}: {result}")
            print(f"  Input Array: {arr}")
            print(f"  Target: {target}, k: {k}")
            print(f"  Expected: {expected}")
            print(f"  Actual: {actual}")
            print("")

        except Exception as e:
            failed_tests += 1
            print(f"Test #{i}: ❌ ERROR")
            print(f"  Input Array: {arr}")
            print(f"  Target: {target}, k: {k}")
            print(f"  Expected: {expected}")
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
