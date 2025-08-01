class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def longest_aligned_chain(root):
    res = 0

    def dfs(node, depth):
        nonlocal res
        if not node:
            return 0

        left_chain = dfs(node.left, depth + 1)
        right_chain = dfs(node.right, depth + 1)

        current_chain = 0

        if node.val == depth:
            current_chain = max(left_chain, right_chain) + 1
            res = max(res, current_chain)
        return current_chain

    dfs(root, 0)

    return res


def run_tests():
    tests = [
        # Test 1: from the book
        (
            Node(
                7,
                Node(1, Node(2, Node(4), Node(3)), Node(8)),
                Node(3, Node(2, Node(3))),
            ),
            3,
        ),
        # Test 2
        (Node(0, Node(1, Node(2, Node(3), None), Node(4)), Node(5)), 4),
        # Test 3: Empty tree
        (None, 0),
        # Test 4: Single node aligned at root
        (Node(0), 1),
        # Test 5: Single node not aligned
        (Node(1), 0),
        # Test 6: Multiple valid chains, should return longest
        (Node(0, Node(1, Node(2, Node(4), None), Node(2, Node(3), None))), 4),
        # Test 7: No aligned nodes
        (Node(5, Node(4, Node(3), Node(3)), Node(2)), 0),
        # Test 8
        (Node(0, Node(1), Node(1)), 2),
    ]

    passed = 0
    failed = 0

    print("🔍 Running Aligned Chain Tree Tests...\n")

    for i, (root, expected) in enumerate(tests, 1):
        result = longest_aligned_chain(root)
        status = "✅ PASSED" if result == expected else "❌ FAILED"
        if result == expected:
            passed += 1
        else:
            failed += 1

        print(f"Test {i}: {status}")
        print(f"  Expected:  {expected}")
        print(f"  Got:       {result}")
        if root is None:
            print("  Tree:      None")
        else:
            print(f"  Root Val:  {root.val}")
        print()

    print("📊 Summary")
    print(f"  Total:  {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")


run_tests()
