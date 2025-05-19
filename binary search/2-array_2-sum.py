def two_array_two_sum(s_arr, u_arr):

    def isPresent(val):
        l = 0
        r = len(s_arr) - 1

        if s_arr[l] >= val or s_arr[r] < val:
            if s_arr[l] == val:
                return 0
            return -1

        while r - l > 1:
            mid = (l + r) // 2
            if s_arr[mid] < val:
                l = mid
            else:
                r = mid

        if s_arr[r] == val:
            return r

        return -1

    for i, val in enumerate(u_arr):
        idx = isPresent(-val)
        if idx != -1:
            return [idx, i]

    return [-1, -1]


def run_tests():
    tests = [
        # Example from book
        ([-5, -4, -1, 4, 6, 6, 7], [-3, 7, 18, 4, 6], [1, 3]),
        # Edge case - empty arrays
        ([], [], [-1, -1]),
        # Edge case - no solution
        ([1, 2], [3, 4], [-1, -1]),
        # Edge case - solution at start
        ([1], [-1], [0, 0]),
        # Edge case - solution at end
        ([1, 2], [-2, -1], [1, 0]),
    ]

    passed = 0
    failed = 0

    print("Running tests:")
    print("-" * 50)

    for i, (sorted_arr, unsorted_arr, want) in enumerate(tests, 1):
        got = two_array_two_sum(sorted_arr, unsorted_arr)
        test_name = f"Test #{i}"

        try:
            assert got == want, f"got: {got}, want: {want}"
            print(f"✅ {test_name} PASSED")
            print(f"   Input: sorted_arr={sorted_arr}, unsorted_arr={unsorted_arr}")
            print(f"   Expected: {want}")
            print(f"   Got: {got}")
            passed += 1
        except AssertionError as e:
            print(f"❌ {test_name} FAILED: {e}")
            print(f"   Input: sorted_arr={sorted_arr}, unsorted_arr={unsorted_arr}")
            print(f"   Expected: {want}")
            print(f"   Got: {got}")
            failed += 1

        print("-" * 50)

    print(f"Summary: {passed} passed, {failed} failed")


run_tests()
