def process_operations(nums, operations):
    sorted_nums = sorted([(n, i) for i, n in enumerate(nums)])

    c = 0
    deleted_idx = set()
    for op in operations:
        if op >= 0:
            nums[op] = None
            deleted_idx.add(op)
        if op == -1:
            curr_smallest_idx = sorted_nums[c][1]
            while curr_smallest_idx in deleted_idx:
                c += 1
                curr_smallest_idx = sorted_nums[c][1]
            nums[curr_smallest_idx] = None
            c += 1
    return [n for n in nums if n is not None]


def run_tests():
    tests = [
        ([50, 30, 70, 20, 80], [2, -1, 4, -1], [50]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([1, 2, 3], [-1, -1, -1], []),
        ([1, 2, 3], [0, 1, 2], []),
        ([1], [-1], []),
        ([5, 5, 5], [-1, -1], [5]),
        ([-3, -2, -1], [-1, -1], [-1]),
        ([10, 10, 20, 20], [1, -1, -1], [20]),
        ([1, 2, 3], [0, 0, 0], [2, 3]),
        ([5, 4, 3, 2, 1], [2, -1, 0, -1], [4]),
        ([10**9, -(10**9), 0], [-1, -1], [10**9]),
    ]

    passed = 0
    failed = 0

    print("🔍 Running process_operations Tests...\n")

    for i, (nums, operations, expected) in enumerate(tests, 1):
        result = process_operations(
            nums.copy(), operations.copy()
        )  # Use copy to avoid mutation
        if result == expected:
            status = "✅ PASSED"
            passed += 1
        else:
            status = "❌ FAILED"
            failed += 1

        print(f"Test {i}: {status}")
        print(f"  Input nums:       {nums}")
        print(f"  Input operations: {operations}")
        print(f"  Expected:         {expected}")
        print(f"  Got:              {result}")
        print()

    print("📊 Summary")
    print(f"  Total:  {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")


run_tests()
