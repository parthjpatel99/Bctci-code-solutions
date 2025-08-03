from collections import deque, defaultdict


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def zig_zag_order(root):
    if not root:
        return []
    curr_level = []
    res = []
    curr_depth = 0
    queue = deque([(root, 0)])
    while queue:
        node, depth = queue.popleft()
        if not node:
            continue

        if depth > curr_depth:
            if curr_depth % 2 == 0:
                res += curr_level
            else:
                res += curr_level[::-1]
            curr_level = []
            curr_depth = depth
        curr_level.append(node)
        queue.append((node.left, depth + 1))
        queue.append((node.right, depth + 1))

    if curr_depth % 2 == 0:
        res += curr_level
    else:
        res += curr_level[::-1]

    return res


def run_tests():
    # Example 1 from the book
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.left = Node(6)
    root1.right.right = Node(7)

    # Example 2 - empty tree
    root2 = None

    # Example 3 - single node
    root3 = Node(1)

    # Example 4 - unbalanced tree
    root4 = Node(1)
    root4.left = Node(2)
    root4.left.left = Node(3)
    root4.left.left.left = Node(4)

    # Example 5 - complete binary tree
    root5 = Node(1)
    root5.left = Node(2)
    root5.right = Node(3)
    root5.left.left = Node(4)
    root5.left.right = Node(5)
    root5.right.left = Node(6)
    root5.right.right = Node(7)
    root5.left.left.left = Node(8)
    root5.left.left.right = Node(9)
    root5.left.right.left = Node(10)
    root5.left.right.right = Node(11)
    root5.right.left.left = Node(12)
    root5.right.right.left = Node(14)
    root5.right.right.right = Node(15)

    tests = [
        ("Basic tree", root1, [1, 3, 2, 4, 5, 6, 7]),
        ("Empty tree", root2, []),
        ("Single node", root3, [1]),
        ("Unbalanced left-heavy tree", root4, [1, 2, 3, 4]),
        (
            "Complete binary tree",
            root5,
            [1, 3, 2, 4, 5, 6, 7, 15, 14, 12, 11, 10, 9, 8],
        ),
    ]

    passed = 0

    print("🧪 Running tests for `zig_zag_order()`\n")

    for i, (desc, root, want) in enumerate(tests, 1):
        got = [node.val for node in zig_zag_order(root)]
        passed_flag = got == want
        print(f"Test {i}: {desc}")
        print(f"   {'✅ PASSED' if passed_flag else '❌ FAILED'}")
        print(f"   Expected Output: {want}")
        print(f"   Actual Output  : {got}")
        print("-" * 40)
        if passed_flag:
            passed += 1

    total = len(tests)
    print("\n📊 Summary")
    print(f"   Total tests : {total}")
    print(f"   Passed      : {passed}")
    print(f"   Failed      : {total - passed}")


run_tests()
