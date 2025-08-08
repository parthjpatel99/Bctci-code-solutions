class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def has_duplicate(root):
    prev = float("-inf")
    res = False

    def dfs(node):
        nonlocal prev, res
        if not node or res:
            return
        dfs(node.left)
        if prev == node.val:
            res = True
        prev = node.val
        dfs(node.right)

    dfs(root)
    return res


def run_tests():
    class Colors:
        GREEN = "\033[92m"
        RED = "\033[91m"
        END = "\033[0m"

    # Example 1 - BST with duplicates
    root1 = Node(5, Node(2, None, Node(4)), Node(9, Node(9, None, Node(9)), Node(11)))

    # Example 2 - empty tree
    root2 = None

    # Example 3 - single node
    root3 = Node(1)

    # Example 4 - BST without duplicates
    root4 = Node(5, Node(2, Node(1), Node(4)), Node(8, Node(6), Node(9)))

    tests = [
        (root1, True, "Has duplicates (9s)"),
        (root2, False, "Empty tree"),
        (root3, False, "Single node"),
        (root4, False, "No duplicates"),
    ]

    passed = 0
    print("Running has_duplicate Tests...\n")

    for i, (root, want, desc) in enumerate(tests):
        got = has_duplicate(root)
        status = "✅ PASSED" if got == want else "❌ FAILED"
        color = Colors.GREEN if got == want else Colors.RED

        print(f"Test {i + 1}: {color}{status}{Colors.END}")
        print(f"  Description     : {desc}")
        print(f"  Expected output : {want}")
        print(f"  Actual output   : {got}")
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
