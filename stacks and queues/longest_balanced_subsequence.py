def longest_balanced_subsequence(s):
    remove_set = set()
    stack = []

    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if not stack:
                remove_set.add(i)
            else:
                stack.pop()

    while stack:
        remove_set.add(stack.pop())

    res = []
    for i, char in enumerate(s):
        if i not in remove_set:
            res.append(char)
    return "".join(res)


def run_tests():
    tests = [
        ("))(())(()", "(())()"),
        ("(()(()(", "()()"),
        ("())(()", "()()"),
        ("(", ""),
        ("", ""),
    ]

    passed = 0
    failed = 0

    print("🔍 Running Longest Balanced Subsequence Tests...\n")

    for i, (s, expected) in enumerate(tests, 1):
        result = longest_balanced_subsequence(s)
        if result == expected:
            status = "✅ PASSED"
            passed += 1
        else:
            status = "❌ FAILED"
            failed += 1

        print(f"Test {i}: {status}")
        print(f"  Input:     {repr(s)}")
        print(f"  Expected:  {expected}")
        print(f"  Got:       {result}")
        print()

    print("📊 Summary")
    print(f"  Total:  {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")


run_tests()
