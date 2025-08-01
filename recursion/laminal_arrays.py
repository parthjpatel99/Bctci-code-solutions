def max_laminal_sum(arr):
    def helper(start, end):
        if start == end:
            return arr[start]

        mid = (start + end) // 2
        left_max = helper(start, mid)
        right_max = helper(mid + 1, end)
        total = sum(arr[start : end + 1])

        return max(left_max, right_max, total)

    return helper(0, len(arr) - 1)


def run_tests():
    tests = [
        ([3, -9, 2, 4, -1, 5, 5, -4], 6),
        ([1], 1),
        ([-1, -2], -1),
        ([1, 2, 3, 4], 10),
        ([-2, -1, -4, -3], -1),
        (
            [
                1,
                -2,
                3,
                -4,
                5,
                -6,
                7,
                -8,
                9,
                -10,
                11,
                -12,
                13,
                -14,
                15,
                -16,
                17,
                -18,
                19,
                -20,
            ],
            19,
        ),
        ([i if i % 2 == 0 else -i for i in range(1, 10001)], 10000),
    ]

    passed = 0
    failed = 0

    print("🔍 Running Max Laminal Subsequence Tests...\n")

    for i, (arr, expected) in enumerate(tests, 1):
        result = max_laminal_sum(arr)
        status = "✅ PASSED" if result == expected else "❌ FAILED"
        if result == expected:
            passed += 1
        else:
            failed += 1

        arr_str = str(arr[:10]) + ("..." if len(arr) > 10 else "")

        print(f"Test {i}: {status}")
        print(f"  Input:     {arr_str}")
        print(f"  Expected:  {expected}")
        print(f"  Got:       {result}")
        print()

    print("📊 Summary")
    print(f"  Total:  {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")


run_tests()
