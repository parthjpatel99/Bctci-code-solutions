from collections import defaultdict


def largest_set_intersection(sets):
    k = len(sets)
    if k == 1:
        return 0

    count = defaultdict(int)

    for s in sets:
        for n in s:
            count[n] += 1

    # Elements in elems occur k-1 times across all the sets.
    elems = set()

    for key, value in count.items():
        if value == k - 1:
            elems.add(key)

    # For each set, we track the sum of occurence of the elements in elems
    # We return the index of the set that has minimum such number.
    # OR
    # For each set, we store the number of elements in elems that have count = 0 ?
    # We return the index of the set where elements in elems appear 0 times ?

    res = 0
    min_count = float("inf")

    for i, s in enumerate(sets):
        count = sum(1 for num in s if num in elems)
        if count < min_count:
            min_count = count
            res = i

    return res


def run_tests():
    tests = [
        # Example 1 from the book
        ([[1, 2, 3], [3, 2, 1], [1, 4, 5], [1, 2]], 2),
        # Example 2 from the book
        ([[1, 2], [3, 4], [5, 6]], 0),
        # Example 3 from the book
        ([[1, 2], [3, 4, 5]], 0),
        # Example 4 from the book
        ([[1, 2, 3]], 0),
        # Additional test cases
        ([[1], [1]], 0),
        ([[1, 2], [2, 3], [1, 3]], 0),
    ]

    all_passed = True

    for i, (sets, want) in enumerate(tests, 1):
        got = largest_set_intersection(sets)
        passed = got == want
        status_icon = "✅" if passed else "❌"
        print(f"{status_icon} Test Case {i}: {'PASSED' if passed else 'FAILED'}")
        print(f"   ➤ Input: {sets}")
        print(f"   ➤ Expected Output: {want}")
        print(f"   ➤ Actual Output:   {got}\n")

        if not passed:
            all_passed = False

    print("🎉 All tests passed!" if all_passed else "🚨 Some tests failed.")


run_tests()
