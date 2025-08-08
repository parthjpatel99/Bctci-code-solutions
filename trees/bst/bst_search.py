class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


"""
def contains_target(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    elif target < root.val:
        return contains_target(root.left, target)
    else:
        return contains_target(root.right, target)
"""


def contains_target(root, target):
    curr = root
    while curr:
        if curr.val == target:
            return True
        if target < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    return False


def run_tests():
    # Test 1
    root1 = Node(5, Node(2, None, Node(4)), Node(9, Node(9, None, Node(9)), Node(11)))

    # Test 2: Empty tree
    root2 = None

    # Test 3: Single node
    root3 = Node(1)

    # Test 4: Perfect BST
    root4 = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))

    # Test 5: Unbalanced BST
    root5 = Node(5, Node(3, Node(2, Node(1), None), Node(4)), None)

    tests = [
        ("Tree with multiple 9s", root1, 6, False),
        ("Tree with multiple 9s", root1, 9, True),
        ("Tree with multiple 9s", root1, 3, False),
        ("Tree with multiple 9s", root1, 4, True),
        ("Empty tree", root2, 1, False),
        ("Single node = 1", root3, 1, True),
        ("Single node = 1", root3, 2, False),
        ("Perfect BST", root4, 5, True),
        ("Perfect BST", root4, 8, False),
        ("Unbalanced BST", root5, 1, True),
        ("Unbalanced BST", root5, 5, True),
        ("Unbalanced BST", root5, 6, False),
    ]

    passed = 0
    total = len(tests)

    print("🧪 Running tests for `contains_target()`\n")

    for i, (desc, root, target, want) in enumerate(tests, 1):
        got = contains_target(root, target)
        success = got == want
        print(f"Test {i}: {desc}")
        print(f"   Target        : {target}")
        print(f"   Expected      : {want}")
        print(f"   Got           : {got}")
        print(f"   Result        : {'✅ PASSED' if success else '❌ FAILED'}")
        print("-" * 40)
        if success:
            passed += 1

    print("\n📊 Summary")
    print(f"   Total tests : {total}")
    print(f"   Passed      : {passed}")
    print(f"   Failed      : {total - passed}")


run_tests()
