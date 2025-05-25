import collections

class Checker:
    def __init__(self, s):
        self.s = s

    def expands_into(self, s2):
        if len(s2) - len(self.s) != 1:
            return False
        
        freq = collections.defaultdict(int)

        for c in s2:
            freq[c] += 1

        for c in self.s:
            if c not in freq:
                return False
            freq[c] -= 1
            if freq[c] == 0:
                del freq[c]
            
        return len(freq) == 1 and list(freq.values())[0] == 1


def run_tests():
    tests = [
        # Example 1 from the book
        ("tea", [
            ("tea", False),
            ("team", True),
            ("seam", False),
        ]),
        # Example 2 from the book
        ("on", [
            ("nooo", False),
            ("not", True),
            ("now", True),
        ]),
        # Additional test cases
        ("", [
            ("a", True),
            ("", False),
            ("ab", False),
        ]),
        ("xyz", [
            ("wxyz", True),
            ("xyzw", True),
            ("xyza", True),
            ("xyz", False),
        ]),
    ]

    test_num = 1
    passed = 0
    failed = 0

    for s, checks in tests:
        checker = Checker(s)
        print(f"\nChecker base string: '{s}'")
        for s2, want in checks:
            got = checker.expands_into(s2)
            status = "✅" if got == want else "❌"
            print(f"Test {test_num}: {status}")
            print(f"  Input: {repr(s2)}")
            print(f"  Expected Output: {want}")
            print(f"  Actual Output:   {got}")
            print("-" * 40)

            if got == want:
                passed += 1
            else:
                failed += 1
            test_num += 1

    total = passed + failed
    print("\nSUMMARY")
    print("=" * 40)
    print(f"Total tests: {total}")
    print(f"Passed:      {passed}")
    print(f"Failed:      {failed}")
    print("=" * 40)


run_tests()