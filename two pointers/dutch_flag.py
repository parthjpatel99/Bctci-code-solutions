def sort_colors_counting_sort(arr):
    countR = countW = 0
    for c in arr:
        if c == "R":
            countR += 1
        elif c == "W":
            countW += 1
    i = 0
    while i < len(arr):
        if i < countR:
            arr[i] = "R"
        elif i < countR + countW:
            arr[i] = "W"
        else:
            arr[i] = "B"

        i += 1


def sort_colors_two_pointers(arr):
    # First pass: move all 'R' to the left
    left = 0
    for i in range(len(arr)):
        if arr[i] == "R":
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    # Second pass: move all 'W' to the middle
    right = left
    for i in range(left, len(arr)):
        if arr[i] == "W":
            arr[right], arr[i] = arr[i], arr[right]
            right += 1


def run_tests():
    tests = [
        # Example from the book
        (list("RWBBWRW"), list("RRWWWBB")),
        # Additional test cases
        ([], []),
        (list("R"), list("R")),
        (list("W"), list("W")),
        (list("B"), list("B")),
        (list("RW"), list("RW")),
        (list("WR"), list("RW")),
        (list("RWB"), list("RWB")),
        (list("RRRWWBBB"), list("RRRWWBBB")),
        (list("BBBWWRRR"), list("RRRWWBBB")),
    ]

    # Test counting sort implementation
    print("Testing sort_colors_counting_sort:")
    print("-" * 50)

    passed_counting = 0
    failed_counting = 0

    for i, (arr, want) in enumerate(tests, 1):
        arr_copy = arr.copy()  # Make a copy since function modifies in place
        sort_colors_counting_sort(arr_copy)
        test_name = f"Test #{i}"

        try:
            assert arr_copy == want, f"got: {arr_copy}, want: {want}"
            print(f"✅ {test_name} PASSED")
            print(f"   Input: arr={arr}")
            print(f"   Expected: {want}")
            print(f"   Got: {arr_copy}")
            passed_counting += 1
        except AssertionError as e:
            print(f"❌ {test_name} FAILED: {e}")
            print(f"   Input: arr={arr}")
            print(f"   Expected: {want}")
            print(f"   Got: {arr_copy}")
            failed_counting += 1

        print("-" * 50)

    print(
        f"Summary (counting sort): {passed_counting} passed, {failed_counting} failed"
    )
    print("\n")

    # Test two pointers implementation
    print("Testing sort_colors_two_pointers:")
    print("-" * 50)

    passed_pointers = 0
    failed_pointers = 0

    for i, (arr, want) in enumerate(tests, 1):
        arr_copy = arr.copy()  # Make a copy since function modifies in place
        sort_colors_two_pointers(arr_copy)
        test_name = f"Test #{i}"

        try:
            assert arr_copy == want, f"got: {arr_copy}, want: {want}"
            print(f"✅ {test_name} PASSED")
            print(f"   Input: arr={arr}")
            print(f"   Expected: {want}")
            print(f"   Got: {arr_copy}")
            passed_pointers += 1
        except AssertionError as e:
            print(f"❌ {test_name} FAILED: {e}")
            print(f"   Input: arr={arr}")
            print(f"   Expected: {want}")
            print(f"   Got: {arr_copy}")
            failed_pointers += 1

        print("-" * 50)

    print(f"Summary (two pointers): {passed_pointers} passed, {failed_pointers} failed")
    print(
        f"Overall: {passed_counting + passed_pointers} passed, {failed_counting + failed_pointers} failed"
    )


run_tests()
