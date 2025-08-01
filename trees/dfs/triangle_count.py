class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def triangle_count(root):
    res = 0

    def dfs(node):
        nonlocal res
        if not node:
            return 0, 0

        left_side, _ = dfs(node.left)
        _, right_side = dfs(node.right)

        res += min(left_side, right_side)

        return (left_side + 1, right_side + 1)

    dfs(root)
    return res


def run_tests():
    tests = [
        # Example: full binary tree (4 triangles)
        (Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7))), 4),
        (None, 0),  # Empty tree
        (Node(1), 0),  # Single node
        # No triangles - only left children
        (Node(1, Node(2, Node(3), None), None), 0),
        # No triangles - only right children
        (Node(1, None, Node(2, None, Node(3))), 0),
        # One triangle
        (Node(1, Node(2), Node(3)), 1),
    ]

    passed = 0
    failed = 0

    print("🔍 Running Triangle Count Tests...\n")

    for i, (root, expected) in enumerate(tests, 1):
        result = triangle_count(root)
        status = "✅ PASSED" if result == expected else "❌ FAILED"

        if result == expected:
            passed += 1
        else:
            failed += 1

        print(f"Test {i}: {status}")
        print(f"  Root:      {root.val if root else 'None'}")
        print(f"  Expected:  {expected}")
        print(f"  Got:       {result}")
        print()

    print("📊 Summary")
    print(f"  Total:  {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")


run_tests()
