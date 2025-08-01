class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def invert(root):

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        dfs(node.right)
        node.left, node.right = node.right, node.left

    dfs(root)
    return root


def run_tests():
    # Test 1: Tree with multiple levels
    root1a = Node(
        1,
        Node(6, Node(4, None, Node(5)), Node(11)),
        Node(7, Node(2, None, Node(9)), None),
    )
    root1b = Node(1)
    root1b.left = Node(7)
    root1b.right = Node(6)
    root1b.left.right = Node(2)
    root1b.left.right.left = Node(9)
    root1b.right.left = Node(11)
    root1b.right.right = Node(4)
    root1b.right.right.left = Node(5)

    # Test 2: Empty tree
    root2 = None

    # Test 3: Single node
    root3 = Node(1)

    # Test 4: Left- and right-skewed versions
    root4a = Node(1, Node(2, Node(3), None), None)
    root4b = Node(1, None, Node(2, None, Node(3)))

    tests = [
        (root1a, root1b),  # Full tree inversion
        (root2, None),  # Empty tree
        (root3, root3),  # Single node
        (root4a, root4b),  # Left-right skewed symmetric test
    ]

    def same_values(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (
            t1.val == t2.val
            and same_values(t1.left, t2.left)
            and same_values(t1.right, t2.right)
        )

    passed = 0
    failed = 0

    print("🔍 Running Invert Tree Tests...\n")

    for i, (root, expected) in enumerate(tests, 1):
        result = invert(root)
        ok = same_values(result, expected)
        status = "✅ PASSED" if ok else "❌ FAILED"
        if ok:
            passed += 1
        else:
            failed += 1

        print(f"Test {i}: {status}")
        print(f"  Root Input:  {root.val if root else 'None'}")
        print(f"  Match:       {ok}")
        print()

    print("📊 Summary")
    print(f"  Total:  {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")


run_tests()
