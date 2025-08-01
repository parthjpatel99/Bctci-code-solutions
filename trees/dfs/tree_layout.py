class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def most_stacked(root):
    res = 0
    amap = dict()

    def dfs(node, r, c):
        nonlocal res
        if not node:
            return

        if (r, c) not in amap:
            amap[(r, c)] = 1
        else:
            amap[(r, c)] += 1

        res = max(res, amap[(r, c)])

        dfs(node.left, r + 1, c)
        dfs(node.right, r, c + 1)

    dfs(root, 0, 0)

    return res


def run_tests():
    # Test 1: Example from the book - two nodes stacked
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.left.left.right = Node(7)
    root1.right.left = Node(6)
    root1.right.left.left = Node(8)
    root1.right.left.right = Node(9)

    # Test 2: Single node
    root2 = Node(1)

    # Test 3: Two-level tree
    root3 = Node(1, Node(2), Node(3))

    # Test 4: Perfect binary tree of depth 4 with some stacking
    root4 = Node(
        1,
        Node(
            2,
            Node(4, Node(8), Node(9, None, Node(16))),
            Node(5, Node(10, None, Node(17)), Node(11, Node(18), None)),
        ),
        Node(
            3,
            Node(6, Node(12), Node(13)),
            Node(7, Node(14, Node(19), None), Node(15, Node(20), None)),
        ),
    )

    tests = [
        (root1, 2),  # Example from book
        (root2, 1),  # Single node
        (root3, 1),  # Two-level tree
        (root4, 4),  # Tree with max stacking of 4
    ]

    passed = 0
    failed = 0

    print("🔍 Running Most Stacked Tree Tests...\n")

    for i, (root, expected) in enumerate(tests, 1):
        result = most_stacked(root)
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
