def blocks(n):
    memo = dict()

    def roof(n):
        if n == 1:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = 2 * roof(n - 1) + 1
        return memo[n]

    def blocks_rec(n):
        if n == 1:
            return 1
        return 2 * blocks_rec(n - 1) + roof(n)

    return blocks_rec(n)


def run_tests():
    tests = [
        # Test cases derived from problem description
        (1, 1),
        (2, 5),
        (3, 17),
        (4, 49),
        (5, 129),
        (6, 321),
        (7, 769),
        (8, 1793),
        (9, 4097),
        (10, 9217),
        # Additional test cases
        (100, 125497409422594710748173617332225),
        (
            900,
            7598988535855408903532055466239174868167099937703571974288586838639677414375930378680017808688060990676996497583010538917043687295886628767811752666210922874250234062641689130683034150257717928106700566151709734005265238962938464051451500991865052677825522947633063368065025,
        ),
    ]

    passed = 0
    failed = 0

    print("🔍 Running Blocks(n) Tests...\n")

    for i, (n, expected) in enumerate(tests, 1):
        result = blocks(n)
        if result == expected:
            status = "✅ PASSED"
            passed += 1
        else:
            status = "❌ FAILED"
            failed += 1

        print(f"Test {i}: {status}")
        print(f"  Input n:    {n}")
        print(f"  Expected:   {expected}")
        print(f"  Got:        {result}")
        print()

    print("📊 Summary")
    print(f"  Total:  {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")


run_tests()
