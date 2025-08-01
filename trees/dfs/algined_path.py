class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def aligned_path(root):
    res = 0

    def dfs(node, depth):
        nonlocal res
        if not node:
            return 0

        left_path = dfs(node.left, depth + 1)
        right_path = dfs(node.right, depth + 1)

        curr_path = 0
        if node.val == depth:
            curr_path = 1 + max(left_path, right_path)
            res = max(res, left_path + right_path + 1)

        return curr_path

    dfs(root, 0)

    return res


def run_tests():
    tests = [
        # Test 1: Example from the book
        (
            Node(
                7,
                Node(1, Node(2, Node(4), Node(3)), Node(8)),
                Node(3, Node(2, Node(3), Node(3))),
            ),
            3,
        ),
        # Variation 1
        (
            Node(
                7,
                Node(1, Node(20, Node(4), Node(3)), Node(8)),
                Node(3, Node(2, Node(3), Node(3))),
            ),
            3,
        ),
        # Variation 2
        (
            Node(
                7,
                Node(1, Node(2, Node(4), Node(3)), Node(8)),
                Node(3, Node(20, Node(3), Node(3))),
            ),
            3,
        ),
        # Variation 3
        (
            Node(
                7,
                Node(1, Node(20, Node(4), Node(3)), Node(8)),
                Node(3, Node(20, Node(3), Node(3))),
            ),
            1,
        ),
        # Test 2: Empty tree
        (None, 0),
        # Test 3: Single aligned node
        (Node(0), 1),
        # Test 4: Single unaligned node
        (Node(1), 0),
        # Test 5: Path through root
        (Node(0, Node(1), Node(1)), 3),
        # Test 6: No aligned nodes
        (Node(5, Node(4), Node(2)), 0),
        # Test 7
        (Node(0, Node(1, Node(2), Node(2)), Node(1)), 4),
    ]

    passed = 0
    failed = 0

    print("🔍 Running Aligned Path Tests...\n")

    for i, (root, expected) in enumerate(tests, 1):
        result = aligned_path(root)
        status = "✅ PASSED" if result == expected else "❌ FAILED"

        if result == expected:
            passed += 1
        else:
            failed += 1

        root_val = root.val if root else "None"

        print(f"Test {i}: {status}")
        print(f"  Root:      {root_val}")
        print(f"  Expected:  {expected}")
        print(f"  Got:       {result}")
        print()

    print("📊 Summary")
    print(f"  Total:  {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")


run_tests()
