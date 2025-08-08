class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def is_bst(root):
    prev_value = float("-inf")
    res = True

    def dfs(node):
        nonlocal prev_value, res
        if not node or not res:
            return
        dfs(node.left)
        if node.val < prev_value:
            res = False
        else:
            prev_value = node.val
        dfs(node.right)

    dfs(root)
    return res


def run_tests():
    class Colors:
        GREEN = "\033[92m"
        RED = "\033[91m"
        END = "\033[0m"

    # Example 1 - valid BST
    root1 = Node(5, Node(2, None, Node(4)), Node(9, Node(9, None, Node(9)), Node(11)))

    # Example 2 - empty tree
    root2 = None

    # Example 3 - single node
    root3 = Node(1)

    # Example 4 - invalid BST (right child smaller than parent)
    root4 = Node(5, Node(2), Node(4))

    # Example 5 - invalid BST (left child larger than parent)
    root5 = Node(5, Node(6), Node(7))

    tests = [
        (root1, True, "Valid BST"),
        (root2, True, "Empty tree"),
        (root3, True, "Single node"),
        (root4, False, "Right child < parent"),
        (root5, False, "Left child > parent"),
    ]

    passed = 0

    print("Running is_bst Tests...\n")

    for i, (root, want, desc) in enumerate(tests):
        got = is_bst(root)
        status = "✅ PASSED" if got == want else "❌ FAILED"
        color = Colors.GREEN if got == want else Colors.RED

        print(f"Test {i + 1}: {color}{status}{Colors.END}")
        print(f"  Description       : {desc}")
        print(f"  Expected output   : {want}")
        print(f"  Actual output     : {got}")
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
