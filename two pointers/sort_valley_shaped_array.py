def sort_valley_array(arr):
    res = [0] * len(arr)
    l = 0
    r = c = len(arr) - 1

#   Potential gotchya here, l <= r as l might cross over 
    while l <= r:
        if arr[l] > arr[r]:
            res[c] = arr[l]
            c-=1
            l+=1
        else:
            res[c] = arr[r]
            r-=1
            c-=1

    return res

def run_tests():
    tests = [
        # Example 1 from the book
        ([8, 4, 2, 6], [2, 4, 6, 8]),
        # Example 2 from the book
        ([1, 2], [1, 2]),
        # Example 3 from the book
        ([2, 2, 1, 1], [1, 1, 2, 2]),
        # Additional test cases
        ([], []),
        ([1], [1]),
        ([3, 2, 1, 4], [1, 2, 3, 4]),
        ([5, 4, 3, 2, 1, 2, 3], [1, 2, 2, 3, 3, 4, 5]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
    ]

    passed = 0
    failed = 0

    print("Running tests:")
    print("-" * 50)

    for i, (arr, want) in enumerate(tests, 1):
        got = sort_valley_array(arr)
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
