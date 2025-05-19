def missing_numbers(arr, low, high):
    if not arr:
        return [c for c in range(low, high + 1)]
    res = []
    l = 0
    while low <= high and l < len(arr):
        if arr[l] < low:
            l += 1
        elif low == arr[l]:
            low += 1
            l += 1
        else:
            res.append(low)
            low += 1

    while low <= high:
        res.append(low)
        low += 1

    return res


def run_tests():
    tests = [
        # Example 1 from the book
        ([6, 9, 12, 15, 18], 9, 13, [10, 11, 13]),
        # Example 2 from the book
        ([], 9, 9, [9]),
        # Example 3 from the book
        ([6, 7, 8, 9], 7, 8, []),
        # Additional test cases
        ([], 1, 5, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 1, 5, []),
        ([1, 3, 5], 1, 5, [2, 4]),
        ([1], 1, 1, []),
        ([2], 1, 3, [1, 3]),
    ]

    passed = 0
    failed = 0

    print("Running tests:")
    print("-" * 50)

    for i, (arr, low, high, want) in enumerate(tests, 1):
        got = missing_numbers(arr, low, high)
        test_name = f"Test #{i}"

        try:
            assert got == want, f"got: {got}, want: {want}"
            print(f"✅ {test_name} PASSED")
            print(f"   Input: arr={arr}, low={low}, high={high}")
            print(f"   Expected: {want}")
            print(f"   Got: {got}")
            passed += 1
        except AssertionError as e:
            print(f"❌ {test_name} FAILED: {e}")
            print(f"   Input: arr={arr}, low={low}, high={high}")
            print(f"   Expected: {want}")
            print(f"   Got: {got}")
            failed += 1

        print("-" * 50)

    print(f"Summary: {passed} passed, {failed} failed")


run_tests()
