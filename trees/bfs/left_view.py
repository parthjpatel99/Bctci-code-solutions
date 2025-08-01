from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def left_view(root):
    if not root:
        return []
    res = []
    queue = deque([(root, 0)])
    aset = set()
    while queue:
        node, depth = queue.popleft()
        if not node:
            continue
        if depth not in aset:
            res.append(node.val)
        aset.add(depth)
        queue.append((node.left, depth + 1))
        queue.append((node.right, depth + 1))

    return res


def run_tests():
    # Test 1
    root1 = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(6)))

    # Test 2: Empty tree
    root2 = None

    # Test 3: Single node
    root3 = Node(1)

    # Test 4: Only right children
    root4 = Node(1, None, Node(2, None, Node(3)))

    # Test 5: Only left children
    root5 = Node(1, Node(2, Node(3), None), None)

    # Test 6: Book example
    root6 = Node(5, Node(2, None, Node(6)), Node(9, Node(9, None, Node(1)), Node(8)))

    tests = [
        ("Example tree", root1, [1, 2, 4]),
        ("Empty tree", root2, []),
        ("Single node", root3, [1]),
        ("Right-skewed tree", root4, [1, 2, 3]),
        ("Left-skewed tree", root5, [1, 2, 3]),
        ("Book example", root6, [5, 2, 6, 1]),
    ]

    passed = 0
    failed = 0

    print("🧪 Running tests for `left_view()`...\n")

    for i, (label, root, want) in enumerate(tests, 1):
        got = left_view(root)
        if got == want:
            print(f"✅ Test {i}: {label} - PASSED")


run_tests()
