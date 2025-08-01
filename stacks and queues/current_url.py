def current_url(actions):
    stack = []

    for action, value in actions:
        if action == "go":
            stack.append(value)
        else:
            while len(stack) > 1 and value > 0:
                stack.pop()
                value -= 1
    return stack[-1]


def run_tests():
    tests = [
        (
            [
                ["go", "google.com"],
                ["go", "wikipedia.com"],
                ["go", "amazon.com"],
                ["back", 4],
                ["go", "youtube.com"],
                ["go", "netflix.com"],
                ["back", 1],
            ],
            "youtube.com",
        ),
        ([["go", "example.com"], ["back", 1]], "example.com"),
        (
            [["go", "site1.com"], ["go", "site2.com"], ["back", 1], ["back", 1]],
            "site1.com",
        ),
    ]

    passed = 0
    failed = 0

    print("🔍 Running Browser Navigation Tests...\n")

    for i, (actions, expected) in enumerate(tests, 1):
        result = current_url(actions)
        if result == expected:
            status = "✅ PASSED"
            passed += 1
        else:
            status = "❌ FAILED"
            failed += 1

        print(f"Test {i}: {status}")
        print(f"  Actions:   {actions}")
        print(f"  Expected:  {expected}")
        print(f"  Got:       {result}")
        print()

    print("📊 Summary")
    print(f"  Total:  {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")


run_tests()
