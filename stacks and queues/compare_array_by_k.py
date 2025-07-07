def compress_array_k(arr, k):
    stack = []
    def merge(num):
        if not stack or stack[-1][0] != num:
            stack.append([num, 1])
        elif stack[-1][1] < k-1:
            stack[-1][1] += 1
        else:
            stack.pop()
            merge(num * k)
    for num in arr:
        merge(num)

    res = []
    for num, count in stack:
        for _ in range(count):
            res.append(num)
    return res


def run_tests():
    tests = [
        ([1, 9, 9, 3, 3, 3, 4], 3, [1, 27, 4]),
        ([8, 4, 2, 2], 2, [16]),
        ([4, 4, 4, 4], 5, [4, 4, 4, 4]),
        ([], 2, []),
        ([0, 0, 0, 0], 2, [0]),
    ]

    passed = 0
    failed = 0

    print("🔍 Running compress_array_k Tests...\n")

    for i, (arr, k, expected) in enumerate(tests, 1):
        result = compress_array_k(arr, k)
        if result == expected:
            status = "✅ PASSED"
            passed += 1
        else:
            status = "❌ FAILED"
            failed += 1

        print(f"Test {i}: {status}")
        print(f"  Input:     arr = {arr}, k = {k}")
        print(f"  Expected:  {expected}")
        print(f"  Got:       {result}")
        print()

    print("📊 Summary")
    print(f"  Total:  {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")

run_tests()