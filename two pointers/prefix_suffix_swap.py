def swap_prefix_suffix(arr):
    n = len(arr)
    p1 = 0
    p2 = n // 3
    p3 = 2 * (n // 3)

    while p1 < n//3 and p2 < 2 *(n//3) and p3 < n:
        arr[p1] , arr[p3] = arr[p3], arr[p1]
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1+=1
        p2+=1
        p3+=1


def run_tests():
    tests = [
        # Example from the book
        (list("badreview"), list("reviewbad")),
        # Additional test cases
        ([], []),
        (list("abc"), list("bca")),
        (list("abcdef"), list("cdefab")),
        (list("123456789"), list("456789123")),
        (list("aaabbbccc"), list("bbbcccaaa")),
    ]

    passed = 0
    failed = 0

    print("Running tests:")
    print("-" * 50)

    for i, (arr, want) in enumerate(tests, 1):
        arr_copy = arr.copy()  # Make a copy since swap_prefix_suffix modifies in place
        swap_prefix_suffix(arr_copy)
        test_name = f"Test #{i}"

        try:
            assert arr_copy == want, f"got: {arr_copy}, want: {want}"
            print(f"✅ {test_name} PASSED")
            print(f"   Input: arr={''.join(arr) if isinstance(arr[0], str) else arr}")
            print(f"   Expected: {''.join(want) if isinstance(want[0], str) else want}")
            print(
                f"   Got: {''.join(arr_copy) if isinstance(arr_copy[0], str) else arr_copy}"
            )
            passed += 1
        except AssertionError as e:
            print(f"❌ {test_name} FAILED: {e}")
            print(f"   Input: arr={''.join(arr) if isinstance(arr[0], str) else arr}")
            print(f"   Expected: {''.join(want) if isinstance(want[0], str) else want}")
            print(
                f"   Got: {''.join(arr_copy) if isinstance(arr_copy[0], str) else arr_copy}"
            )
            failed += 1
        except IndexError:
            # Handle empty arrays gracefully
            if len(arr) == 0 and len(want) == 0:
                print(f"✅ {test_name} PASSED")
                print(f"   Input: arr=[]")
                print(f"   Expected: []")
                print(f"   Got: []")
                passed += 1
            else:
                print(f"❌ {test_name} FAILED: IndexError")
                print(f"   Input: arr={arr}")
                print(f"   Expected: {want}")
                print(f"   Got: Error processing empty array")
                failed += 1

        print("-" * 50)

    print(f"Summary: {passed} passed, {failed} failed")

run_tests()
