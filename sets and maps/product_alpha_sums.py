def alphabetic_sum_product(words, target):
    def alhphasum(word):
        s = 0
        for c in word:
            s += ord(c) - ord("a") + 1
        return s

    sumset = set()
    for word in words:
        sumset.add(alhphasum(word))

    for asum in sumset:
        if target % asum != 0:
            continue
        for bsum in sumset:
            k = target / (asum * bsum)
            if k in sumset:
                return True

    return False

    return


def run_tests():
    tests = [
        # Example 1 from the book
        (["abc", "fg", "hij", "klm", "nop", "qrs", "vwx"], 1620, True),
        # Example 2 from the book
        (["a", "b"], 2, True),
        # Additional test cases
        ([], 1, False),
        (["a"], 1, True),
        (["a", "b", "c"], 6, True),
        (["a", "b", "c"], 7, False),
    ]

    passed = 0

    for i, (words, target, want) in enumerate(tests, 1):
        got = alphabetic_sum_product(words, target)
        status = "✅" if got == want else "❌"
        if got == want:
            passed += 1
        print(f"Test {i}: {status}")
        print(f"Inputs:")
        print(f"  words: {words}")
        print(f"  target: {target}")
        print(f"Expected Output: {want}")
        print(f"Actual Output: {got}")
        print("-" * 40)

    total = len(tests)
    print(f"Summary: {passed}/{total} tests passed.")


run_tests()
