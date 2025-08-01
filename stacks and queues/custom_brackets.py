def balanced_brackets(s, brackets):
    amap = {}
    stack = []
    closing = set()

    for pair in brackets:
        amap[pair[0]] = pair[1]
        closing.add(pair[1])
    
    for char in s:
        if char in amap:
            stack.append(amap[char])
        elif char in closing:
            if not stack or stack[-1] != char:
                return False
            stack.pop()
    return len(stack) == 0



def run_tests():
    tests = [
        ("((a+b)*[c-d]-{e/f})", ["()", "[]", "{}"], True),
        ("()[}", ["()", "[]", "{}"], False),
        ("([)]", ["()", "[]", "{}"], False),
        ("<div> hello :) </div>", ["<>", "()"], False),
        (")))(()((", [")("], True),
        ("", ["()"], True),
        ("(", ["()"], False),
        ("<<>>()[]{}", ["<>", "()", "[]", "{}"], True),
        ("[{()}]", ["()", "[]", "{}"], True),
        ("(()", ["()"], False),
        ("())", ["()"], False),
        ("({)}", ["()", "{}"], False),
        ("a(b)c[d]e", ["()", "[]"], True),
        ("<<>>", ["<>"], True),
    ]

    passed = 0
    failed = 0

    print("🔍 Running Bracket Balance Tests...\n")

    for i, (s, brackets, expected) in enumerate(tests, 1):
        result = balanced_brackets(s, brackets)
        if result == expected:
            status = "✅ PASSED"
            passed += 1
        else:
            status = "❌ FAILED"
            failed += 1

        print(f"Test {i}: {status}")
        print(f"  Input:     {repr(s)}")
        print(f"  Brackets:  {brackets}")
        print(f"  Expected:  {expected}")
        print(f"  Got:       {result}")
        print()

    print("📊 Summary")
    print(f"  Total:  {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")

run_tests()