from collections import deque, defaultdict
import math, collections


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def most_protected_node(root):
    if not root:
        return 0
    protection = defaultdict(lambda: math.inf)
    nodes_per_lvl = defaultdict(int)
    node_to_idx = {}

    queue = deque([(root, 0)])
    while queue:
        node, depth = queue.popleft()
        if not node:
            continue
        nodes_per_lvl[depth] += 1
        node_to_idx[node] = nodes_per_lvl[depth] - 1

        protection[node] = min(protection[node], depth, node_to_idx[node])

        queue.append((node.left, depth + 1))
        queue.append((node.right, depth + 1))

    def dfs(node, depth):
        if not node:
            return -1
        left_h = dfs(node.left, depth + 1)
        right_h = dfs(node.right, depth + 1)

        height = max(left_h, right_h) + 1

        protection[node] = min(protection[node], height)
        protection[node] = min(
            protection[node], nodes_per_lvl[depth] - node_to_idx[node] - 1
        )

        return height

    dfs(root, 0)

    return max(protection.values())


def run_tests():
    # Example from the book
    root1 = Node(
        1,
        Node(
            2,
            Node(
                3,
                Node(4, Node(5, Node(6)), Node(7, Node(8), Node(9))),
                Node(10, Node(11)),
            ),
            Node(12, Node(13, Node(14, Node(15), Node(16)))),
        ),
        Node(
            17,
            Node(18, Node(19, Node(20, Node(21)))),
            Node(22, Node(23, Node(24, Node(25)))),
        ),
    )

    def perfect_tree(height):
        if height == 1:
            return Node(1)
        return Node(1, perfect_tree(height - 1), perfect_tree(height - 1))

    tests = [
        ("Book example", root1, 2),
        ("Single node", Node(1), 0),
        ("Linear left tree", Node(1, Node(2, Node(3, Node(4)))), 0),
        ("Perfect binary tree (height 1)", perfect_tree(1), 0),
        ("Perfect binary tree (height 2)", perfect_tree(2), 0),
        ("Perfect binary tree (height 3)", perfect_tree(3), 0),
        ("Perfect binary tree (height 4)", perfect_tree(4), 1),
        ("Perfect binary tree (height 5)", perfect_tree(5), 1),
        ("Perfect binary tree (height 6)", perfect_tree(6), 2),
        ("Perfect binary tree (height 7)", perfect_tree(7), 3),
        ("Perfect binary tree (height 8)", perfect_tree(8), 3),
        ("Perfect binary tree (height 9)", perfect_tree(9), 4),
    ]

    passed = 0
    total = len(tests)

    print("🧪 Running tests for `most_protected_node()`\n")

    for i, (desc, root, want) in enumerate(tests, 1):
        got = most_protected_node(root)
        passed_flag = got == want
        print(f"Test {i}: {desc}")
        print(f"   {'✅ PASSED' if passed_flag else '❌ FAILED'}")
        print(f"   Expected: {want}")
        print(f"   Got     : {got}")
        print("-" * 40)
        if passed_flag:
            passed += 1

    print("\n📊 Summary")
    print(f"   Total tests : {total}")
    print(f"   Passed      : {passed}")
    print(f"   Failed      : {total - passed}")


run_tests()
