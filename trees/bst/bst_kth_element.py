class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def kth_element(root, k):
    steps = 0
    res = None

    def dfs(node):
        nonlocal steps, res
        if not node or res is not None:
            return
        dfs(node.left)
        if steps == k:
            res = node.val
        steps += 1
        dfs(node.right)

    dfs(root)
    return res


def run_tests():
    class Colors:
        GREEN = "\033[92m"
        RED = "\033[91m"
        END = "\033[0m"

    def inorder_values(node):
        """Helper to return an in-order list of node values."""
        if not node:
            return []
        return inorder_values(node.left) + [node.val] + inorder_values(node.right)

    root = Node(5, Node(2, Node(1), Node(4)), Node(8, Node(6), Node(9)))

    tests = [
        (Node(5, Node(2, None, Node(4)), Node(9, Node(9), Node(11))), 4, 9),
        (Node(1), 0, 1),  # Single node
        (root, 0, 1),
        (root, 1, 2),
        (root, 2, 4),
        (root, 3, 5),
        (root, 4, 6),
        (root, 5, 8),
        (root, 6, 9),
    ]

    passed = 0
    print("Running kth_element Tests...\n")

    for i, (tree, k, want) in enumerate(tests):
        got = kth_element(tree, k)
        status = "✅ PASSED" if got == want else "❌ FAILED"
        color = Colors.GREEN if got == want else Colors.RED

        print(f"Test {i + 1}: {color}{status}{Colors.END}")
        print(f"  k value          : {k}")
        print(f"  In-order values  : {inorder_values(tree)}")
        print(f"  Expected output  : {want}")
        print(f"  Actual output    : {got}")
        print("-" * 40)

        if got == want:
            passed += 1

    total = len(tests)
    print(f"\nSummary: {passed}/{total} tests passed.")
    if passed == total:
        print(f"{Colors.GREEN}🎉 All tests passed!{Colors.END}")
    else:
        print(f"{Colors.RED}Some tests failed. Please review above.{Colors.END}")


run_tests()
