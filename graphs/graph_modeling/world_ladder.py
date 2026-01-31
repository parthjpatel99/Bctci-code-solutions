"""
Two friends are playing a game. The first one says a word. Then, the other friend has to form another word by adding or removing a letter. The first friend then needs to find a new word (repetitions are not allowed) by doing the opposite operation (addition or removal). The game goes on, with each friend finding a new word and alternating additions and removals.

These are two examples of games:

    leap, lap, slap, sap, soap, sop, shop, hop
    car, care, are, fare, far, fart, art, cart

However, these are not valid games:

    bounce, ounce, once (we removed a letter twice in a row)
    hung, hug, hung (we repeated a word)
    car, race (we reordered the letters)
    vibes, vibess (vibess is not a real word)

Given two words (strings), word1 and word2, and a list of valid words, words, which contains word1 and word2, return whether it is possible to start the game at word1 and get to word2 using only words from words.

Example 1:
word1 = "leap"
word2 = "hop"
words = [
   "fare", "hug", "car", "vibes", "once", "sop", "far", "ounce", "slap",
    "sap", "cart", "hung", "art", "shop", "fart", "lap", "soap", "are",
   "hop", "care", "leap", "bounce", "beyond", "cracking"
]
Output: True
The game can proceed as:
leap -> lap -> slap -> sap -> soap -> sop -> shop -> hop

Example 2:
word1 = "car"
word2 = "cart"
words = [
   "fare", "hug", "car", "vibes", "once", "sop", "far", "ounce", "slap",
    "sap", "cart", "hung", "art", "shop", "fart", "lap", "soap", "are",
   "hop", "care", "leap", "bounce", "beyond", "cracking"
]
Output: True
The game can proceed as:
car -> care -> are -> fare -> far -> fart -> art -> cart

Example 3:
word1 = "bounce"
word2 = "once"
words = [
   "fare", "hug", "car", "vibes", "once", "sop", "far", "ounce", "slap",
    "sap", "cart", "hung", "art", "shop", "fart", "lap", "soap", "are",
   "hop", "care", "leap", "bounce", "beyond", "cracking"
]
Output: False

Constraints:

    All words contain only lowercase English letters
    All the words in words are unique
    1 <= words.length <= 1000
    1 <= words[i].length <= 30
    word1 and word2 are in words
    word1 and word2 are different
"""


def can_transform(w1, w2):
    if abs(len(w1) - len(w2)) != 1:
        return False
    if len(w1) > len(w2):
        w1, w2 = w2, w1

    for i in range(len(w2)):
        if w1 == w2[:i] + w2[i + 1 :]:
            return True
    return False


def build_graph(words, l1, l2):
    graph = {}
    for word in words:
        if len(word) in (l1, l2):
            graph[word] = []
    for word1 in graph:
        for word2 in graph:
            if word1 != word2 and can_transform(word1, word2):
                graph[word1].append(word2)
    return graph


def has_path(graph, start, end, visited=None):
    if visited is None:
        visited = set()

    if start == end and len(visited) == 0:
        return False
    if start == end and len(visited) > 0:
        return True

    visited.add(start)
    for nbr in graph[start]:
        if nbr not in visited:
            if has_path(graph, nbr, end, visited):
                return True

    return False


def word_ladder_game(word1, word2, words):
    l = len(word1)

    graph1 = build_graph(words, l, l + 1)
    if word2 in graph1 and has_path(graph1, word1, word2):
        return True
    graph2 = build_graph(words, l, l - 1)
    if word2 in graph2 and has_path(graph2, word1, word2):
        return True
    return False


def run_tests():
    tests = [
        # Example 1 from the book
        (
            "leap",
            "hop",
            [
                "fare",
                "hug",
                "car",
                "vibes",
                "once",
                "sop",
                "far",
                "ounce",
                "slap",
                "sap",
                "cart",
                "hung",
                "art",
                "shop",
                "fart",
                "lap",
                "soap",
                "are",
                "hop",
                "care",
                "leap",
                "bounce",
                "beyond",
                "cracking",
            ],
            True,
        ),
        # Example 2 from the book
        (
            "car",
            "cart",
            [
                "fare",
                "hug",
                "car",
                "vibes",
                "once",
                "sop",
                "far",
                "ounce",
                "slap",
                "sap",
                "cart",
                "hung",
                "art",
                "shop",
                "fart",
                "lap",
                "soap",
                "are",
                "hop",
                "care",
                "leap",
                "bounce",
                "beyond",
                "cracking",
            ],
            True,
        ),
        # Invalid - double removal
        ("bounce", "once", ["bounce", "ounce", "once"], False),
        # Invalid - reordered letters
        ("car", "race", ["car", "race"], False),
        # No path exists
        ("cat", "dog", ["cat", "cot", "dot", "dog"], False),
    ]

    passed = 0
    failed = 0

    print("\n=== Running Word Ladder Tests ===\n")

    for i, (word1, word2, words, expected) in enumerate(tests, start=1):
        actual = word_ladder_game(word1, word2, words)
        success = actual == expected

        status = "✅ PASS" if success else "❌ FAIL"
        print(f"Test {i}: {status}")
        print(f"  Inputs:")
        print(f"    word1 = {word1}")
        print(f"    word2 = {word2}")
        print(f"    words = {words}")
        print(f"  Expected Output: {expected}")
        print(f"  Actual Output:   {actual}")
        print("-" * 50)

        if success:
            passed += 1
        else:
            failed += 1

    print("\n=== Summary ===")
    print(f"Total Tests: {len(tests)}")
    print(f"Passed:      {passed}")
    print(f"Failed:      {failed}")


run_tests()
