def valley_bottom(arr):
    def is_before(i):
        return i == 0 or arr[i] < arr[i - 1]

    if len(arr) == 1:
        return arr[0]
    if not arr:
        return -1

    l = 0
    r = len(arr) - 1

    if arr[l] < arr[l + 1]:
        return arr[l]

    if arr[r] < arr[r - 1]:
        return arr[r]

    while r - l > 1:
        mid = (l + r) // 2

        if is_before(mid):
            l = mid
        else:
            r = mid

    return arr[l]


def run_tests():
    tests = [
        # Example 1 from book
        ([6, 5, 4, 7, 9], 4),
        # Example 2 from book
        ([5, 6, 7], 5),
        # Example 3 from book
        ([7, 6, 5], 5),
        # Edge case - 2 elements
        ([2, 1], 1),
        # Edge case - 3 elements
        ([3, 2, 4], 2),
    ]

    passed = 0
    failed = 0

    print("Running tests:")
    print("-" * 50)

    for i, (arr, want) in enumerate(tests, 1):
        got = valley_bottom(arr)
        test_name = f"Test #{i}"

        try:
            assert got == want, f"got: {got}, want: {want}"
            print(f"✅ {test_name} PASSED")
            print(f"   Input: arr={arr}")
            print(f"   Expected: {want}")
            print(f"   Got: {got}")
            passed += 1
        except AssertionError as e:
            print(f"❌ {test_name} FAILED: {e}")
            print(f"   Input: arr={arr}")
            print(f"   Expected: {want}")
            print(f"   Got: {got}")
            failed += 1

        print("-" * 50)

    print(f"Summary: {passed} passed, {failed} failed")


run_tests()
