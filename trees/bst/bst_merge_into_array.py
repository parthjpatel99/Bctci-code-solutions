class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def merge_into_array(root1, root2):
    arr1 = []
    arr2 = []

    def dfs(node, arr):
        if not node:
            return
        dfs(node.left, arr)
        arr.append(node.val)
        dfs(node.right, arr)

    dfs(root1, arr1)
    dfs(root2, arr2)

    res = []

    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    while i < len(arr1):
        res.append(arr1[i])
        i += 1
    while j < len(arr2):
        res.append(arr2[j])
        j += 1
    return res


def run_tests():
    class Colors:
        GREEN = "\033[92m"
        RED = "\033[91m"
        END = "\033[0m"

    def inorder_values(node):
        """Return the in-order traversal of the BST."""
        if not node:
            return []
        return inorder_values(node.left) + [node.val] + inorder_values(node.right)

    root1 = Node(5, Node(2, None, Node(4)), Node(9, Node(9), Node(11)))

    root2 = Node(3, Node(2, Node(1)), Node(7, Node(6), Node(8)))

    root3 = Node(2, Node(2), Node(2))

    root4 = Node(2, Node(2), Node(2))

    tests = [
        # Example 1 from the book
        (root1, root2, [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 9, 11], "Example 1 from book"),
        # Example 2 from the book
        (root3, root4, [2, 2, 2, 2, 2, 2], "Example 2 from book"),
        # Edge cases
        (None, None, [], "Both trees empty"),
        (Node(1), None, [1], "First tree only"),
        (None, Node(1), [1], "Second tree only"),
        (Node(1), Node(2), [1, 2], "Two single-node trees"),
    ]

    passed = 0
    print("Running merge_into_array Tests...\n")

    for i, (t1, t2, want, desc) in enumerate(tests):
        got = merge_into_array(t1, t2)
        status = "✅ PASSED" if got == want else "❌ FAILED"
        color = Colors.GREEN if got == want else Colors.RED

        print(f"Test {i + 1}: {color}{status}{Colors.END}")
        print(f"  Description     : {desc}")
        print(f"  Tree1 in-order  : {inorder_values(t1)}")
        print(f"  Tree2 in-order  : {inorder_values(t2)}")
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
