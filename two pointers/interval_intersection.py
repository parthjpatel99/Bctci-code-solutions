def interval_intersection(arr1, arr2):
    res = []
    p1 = p2 = 0

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1][1] < arr2[p2][0]:
            p1 += 1
        elif arr2[p2][1] < arr1[p1][0]:
            p2 += 1

        else:
            newStart = max(arr1[p1][0], arr2[p2][0])
            newEnd = min(arr1[p1][1], arr2[p2][1])
            res.append([newStart, newEnd])
            if arr1[p1][1] < arr2[p2][1]:
                p1 += 1
            else:
                p2 += 1
    return res


def run_tests():
    tests = [
        # Example 1 from the book
        ([[0, 1], [4, 6], [7, 8]], [[2, 3], [5, 9], [10, 11]], [[5, 6], [7, 8]]),
        # Example 2 from the book
        ([[2, 4], [5, 8]], [[3, 3], [4, 7]], [[3, 3], [4, 4], [5, 7]]),
        # Additional test cases
        ([], [], []),
        ([[1, 2]], [], []),
        ([[1, 3]], [[2, 4]], [[2, 3]]),
        ([[1, 5]], [[2, 3]], [[2, 3]]),
        ([[1, 2], [3, 4]], [[2, 3]], [[2, 2], [3, 3]]),
    ]

    passed = 0
    failed = 0

    print("Running tests:")
    print("-" * 50)

    for i, (arr1, arr2, want) in enumerate(tests, 1):
        got = interval_intersection(arr1, arr2)
        test_name = f"Test #{i}"

        try:
            assert got == want, f"got: {got}, want: {want}"
            print(f"✅ {test_name} PASSED")
            print(f"   Input: arr1={arr1}, arr2={arr2}")
            print(f"   Expected: {want}")
            print(f"   Got: {got}")
            passed += 1
        except AssertionError as e:
            print(f"❌ {test_name} FAILED: {e}")
            print(f"   Input: arr1={arr1}, arr2={arr2}")
            print(f"   Expected: {want}")
            print(f"   Got: {got}")
            failed += 1

        print("-" * 50)

    print(f"Summary: {passed} passed, {failed} failed")


run_tests()
