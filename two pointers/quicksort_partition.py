def partition(arr, pivot):
    l = 0
    r = len(arr) - 1

    while l < r:
        if arr[l] <= pivot:
            l += 1
        elif arr[r] > pivot:
            # Don't forget that we're moving inwards so r -= 1
            r -= 1
        else:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    boundary = 0
    while boundary < len(arr) and arr[boundary] <= pivot:
        boundary += 1

    l = 0
    r = boundary - 1

    while l < r:
        if arr[l] < pivot:
            l += 1
        elif arr[r] == pivot:
            r -= 1

        else:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1


def is_valid_partition(arr, pivot):
    # Find boundaries between sections
    first = 0
    while first < len(arr) and arr[first] < pivot:
        first += 1
    second = first
    while second < len(arr) and arr[second] == pivot:
        second += 1

    # Check that all elements are in their correct sections
    for i in range(first):
        if arr[i] >= pivot:
            return False
    for i in range(first, second):
        if arr[i] != pivot:
            return False
    for i in range(second, len(arr)):
        if arr[i] <= pivot:
            return False
    return True


def run_tests():
    tests = [
        # Example 1 from the book
        ([1, 7, 2, 3, 3, 5, 3], 4),
        # Example 2 from the book
        ([1, 7, 2, 3, 3, 5, 3], 3),
        # Additional test cases
        ([], 1),
        ([1], 1),
        ([1, 2], 1),
        ([2, 1], 1),
        ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 4),
    ]

    passed = 0
    failed = 0

    print("Running tests:")
    print("-" * 50)

    for i, (arr, pivot) in enumerate(tests, 1):
        arr_copy = arr.copy()  # Make a copy since partition modifies in place
        partition(arr_copy, pivot)
        test_name = f"Test #{i}"

        try:
            assert is_valid_partition(arr_copy, pivot), f"Invalid partition"
            print(f"✅ {test_name} PASSED")
            print(f"   Input: arr={arr}, pivot={pivot}")
            print(f"   Result: {arr_copy}")
            print(
                f"   (All elements < {pivot} are on the left, all elements ≥ {pivot} are on the right)"
            )
            passed += 1
        except AssertionError as e:
            print(f"❌ {test_name} FAILED: {e}")
            print(f"   Input: arr={arr}, pivot={pivot}")
            print(f"   Result: {arr_copy}")
            print(f"   (Some elements are not correctly partitioned around {pivot})")
            failed += 1

        print("-" * 50)

    print(f"Summary: {passed} passed, {failed} failed")

run_tests()
