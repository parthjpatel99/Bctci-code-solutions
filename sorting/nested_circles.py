from math import sqrt


def are_circles_nested(circles):
    def contains(c1, c2):
        (x1, y1), r1 = c1
        (x2, y2), r2 = c2

        center_distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        return center_distance + r2 < r1

    circles.sort(key=lambda c: c[1], reverse=True)

    for i in range(len(circles) - 1):
        if not contains(circles[i], circles[i + 1]):
            return False

    return True


def run_tests():
    tests = [
        ([((4, 4), 5), ((8, 4), 2)], False),
        ([((5, 3), 3), ((5, 3), 2), ((4, 4), 5)], True),
        ([((5, 3), 3)], True),
        ([((1, 1), 2), ((1, 1), 2)], False),
        ([((0, 0), 4), ((0, 0), 2)], True),
        ([], True),
        ([((-5, -3), 4), ((-5, -3), 2)], True),
        ([((0, 0), -2)], True),
        ([((10000, 10000), 10000), ((0, 0), 100)], False),
        ([((-10000, -10000), 10000), ((0, 0), 100)], False),
        ([((1, 1), 5), ((1, 1), 4), ((1, 1), 3), ((1, 1), 2)], True),
        ([((0, 0), 2), ((0, 0), 4), ((0, 0), 3)], True),
    ]

    passed = 0
    failed = 0

    print("🔍 Running Circle Nesting Tests...\n")

    for i, (circles, expected) in enumerate(tests, 1):
        result = are_circles_nested(circles)
        if result == expected:
            status = "✅ PASSED"
            passed += 1
        else:
            status = "❌ FAILED"
            failed += 1

        print(f"Test {i}: {status}")
        print(f"  Input:     {circles}")
        print(f"  Expected:  {expected}")
        print(f"  Got:       {result}")
        print()

    print("📊 Summary")
    print(f"  Total:  {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")


run_tests()
