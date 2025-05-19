def sort_even(arr):
    if not arr:
        return []

    l = 0
    r = len(arr) - 1

    while l < r:
        if arr[l] % 2 == 0:
            l += 1
        elif arr[r] % 2 == 1:
            r -= 1
        else:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

def is_valid_solution(arr, original):
    # Check that we have the same elements
    if sorted(arr) != sorted(original):
        return False

    # Find the boundary between even and odd numbers
    boundary = 0
    while boundary < len(arr) and arr[boundary] % 2 == 0:
        boundary += 1

    # Check that all numbers before boundary are even
    # and all numbers after are odd
    for i in range(boundary):
        if arr[i] % 2 != 0:
            return False
    for i in range(boundary, len(arr)):
        if arr[i] % 2 != 1:
            return False
    return True


def run_tests():
    tests = [
        # Example 1 from the book
        ([1, 2, 3, 4, 5], [2, 4, 1, 3, 5]),
        # Example 2 from the book
        ([5, 1, 3, 1, 5], [5, 1, 3, 1, 5]),
        # Additional test cases
        ([], []),
        ([1], [1]),
        ([2], [2]),
        ([1, 2], [2, 1]),
        ([2, 1], [2, 1]),
        ([1, 3, 2, 4], [2, 4, 1, 3]),
    ]

    passed = 0
    failed = 0

    print("Running tests:")
    print("-" * 50)

    for i, (arr, example_solution) in enumerate(tests, 1):
        arr_copy = arr.copy()  # Make a copy since sort_even modifies in place
        sort_even(arr_copy)
        test_name = f"Test #{i}"

        try:
            assert is_valid_solution(
                arr_copy, arr
            ), f"got: {arr_copy}, example solution: {example_solution}"
            print(f"✅ {test_name} PASSED")
            print(f"   Input: arr={arr}")
            print(f"   Example solution: {example_solution}")
            print(f"   Got: {arr_copy}")
            passed += 1
        except AssertionError as e:
            print(f"❌ {test_name} FAILED: {e}")
            print(f"   Input: arr={arr}")
            print(f"   Example solution: {example_solution}")
            print(f"   Got: {arr_copy}")
            failed += 1

        print("-" * 50)

    print(f"Summary: {passed} passed, {failed} failed")


run_tests()
