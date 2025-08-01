def current_url_followup(actions):
    stack = []
    forward_stack = []

    for action, value in actions:
        if action == "go":
            stack.append(value)
            forward_stack.clear()
        elif action == "back":
            while len(stack) > 1 and value > 0:
                forward_stack.append(stack.pop())
                value -= 1
        else:
            while forward_stack and value > 0:
                stack.append(forward_stack.pop())
                value -= 1

    return stack[-1]


def run_tests():
    tests = [
        (
            [
                ["go", "google.com"],
                ["go", "wikipedia.com"],
                ["back", 1],
                ["forward", 1],
                ["back", 3],
                ["go", "netflix.com"],
                ["forward", 3],
            ],
            "netflix.com",
        ),
        ([["go", "example.com"], ["forward", 1]], "example.com"),
        (
            [
                ["go", "site1.com"],
                ["go", "site2.com"],
                ["back", 1],
                ["forward", 1],
                ["back", 1],
            ],
            "site1.com",
        ),
    ]

    passed = 0
    failed = 0

    print("🔍 Running Browser Follow-Up Navigation Tests...\n")

    for i, (actions, expected) in enumerate(tests, 1):
        try:
            result = current_url_followup(actions)
            if result == expected:
                status = "✅ PASSED"
                passed += 1
            else:
                status = "❌ FAILED"
                failed += 1
        except Exception as e:
            result = f"Exception: {e}"
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
