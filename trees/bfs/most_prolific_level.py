from collections import deque, defaultdict


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def most_prolific_level(root):
    if not root:
        return -1
    lvl_count = defaultdict(int)
    queue = deque([(root, 0)])
    while queue:
        node, depth = queue.popleft()
        if not node:
            continue
        lvl_count[depth] += 1
        queue.append((node.left, depth + 1))
        queue.append((node.right, depth + 1))

    res = max_prolificness = -1

    for level in lvl_count:
        if level + 1 not in lvl_count:
            continue
        prolificness = lvl_count[level + 1] / lvl_count[level]

        if prolificness > max_prolificness:
            max_prolificness = prolificness
            res = level

    return res


def print_tree(root):
    """Helper function to print the tree in pre-order format."""
    if not root:
        return "None"
    return f"{root.val}({print_tree(root.left)}, {print_tree(root.right)})"


def run_tests():
    # Define test trees
    root1 = Node(5, Node(2, None, Node(6)), Node(9, Node(9, None, Node(1)), Node(8)))

    root2 = None

    root3 = Node(1)

    root4 = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))

    root5 = Node(1, Node(2, Node(4, Node(8), Node(9)), Node(5)), Node(3))

    root6 = Node(1, Node(2, Node(4, Node(8), Node(9)), Node(5, None, Node(11))), None)

    root7 = Node(1, Node(2, Node(4, Node(8), Node(9))))

    tests = [
        ("Book example", root1, 0),
        ("Empty tree", root2, -1),
        ("Single node", root3, -1),
        ("Perfect binary tree", root4, 0),
        ("Unbalanced tree", root5, 0),
        ("Deep right-heavy node", root6, 1),
        ("Left-skewed deep", root7, 2),
    ]

    passed = 0
    failed = 0

    print("🧪 Running tests for `most_prolific_level()`\n")

    for i, (label, root, want) in enumerate(tests, 1):
        got = most_prolific_level(root)
        passed_flag = got == want
        print(f"Test {i}: {label}")
        print(f"{'✅ PASSED' if passed_flag else '❌ FAILED'}")
        print(f"Input Tree (Pre-order): {print_tree(root)}")
        print(f"Expected Output: {want}")
        print(f"Actual Output  : {got}")
        print("-" * 40)

        if passed_flag:
            passed += 1
        else:
            failed += 1

    print("\n📊 Summary")
    print(f"Total tests : {len(tests)}")
    print(f"Passed      : {passed}")
    print(f"Failed      : {failed}")


run_tests()
