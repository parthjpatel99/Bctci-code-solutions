def letter_occurrences(word):
    """
    Returns a list of unique letters in the word, sorted by their frequency
    in descending order. If two letters have the same frequency, they are
    sorted alphabetically.

    :param word: The input string to analyze.
    :return: A list of unique letters sorted by frequency and alphabetically.
    """
    from collections import Counter

    # Count occurrences of each letter
    letter_count = Counter(word)

    # Sort letters first by frequency (descending), then alphabetically
    sorted_letters = sorted(letter_count.keys(), key=lambda x: (-letter_count[x], x))

    return sorted_letters

def run_tests():
    tests = [
        ("supercalifragilisticexpialidocious", 
         ['i', 'a', 'c', 'l', 's', 'e', 'o', 'p', 'r', 'u', 'd', 'f', 'g', 't', 'x']),
        ("", []),
        ("a", ["a"]),
        ("abc", ["a", "b", "c"]),
        ("aabbbcccc", ["c", "b", "a"]),
        ("zzzzz", ["z"]),
        ("ababab", ["a", "b"]),
        ("zyxwv", ["v", "w", "x", "y", "z"]),
        ("aAaAaA", ["A", "a"]),
        ("aaaaabbbbbbbcccccccccdddddddddddeeeeeeeeeeee",
         ["e", "d", "c", "b", "a"]),
        ("hello world", ["l", "o", " ", "d", "e", "h", "r", "w"]),
    ]

    passed = 0
    failed = 0

    print("🔍 Running Tests...\n")

    for i, (word, expected) in enumerate(tests, 1):
        result = letter_occurrences(word)
        if result == expected:
            status = "✅ PASSED"
            passed += 1
        else:
            status = "❌ FAILED"
            failed += 1

        print(f"Test {i}: {status}")
        print(f"  Input:    {repr(word)}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print()

    print("📊 Summary")
    print(f"  Total: {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")


run_tests()