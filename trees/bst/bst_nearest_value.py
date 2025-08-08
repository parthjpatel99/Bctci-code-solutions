import math


class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def find_closest(root, target):
    curr = root
    below, above = float("-inf"), float("inf")

    while curr:
        if curr.val == target:
            return target
        elif target < curr.val:
            above = curr.val
            curr = curr.left
        else:
            below = curr.val
            curr = curr.right

    if above - target < target - below:
        return above
    else:
        return below


def run_tests():
    class Colors:
        GREEN = "\033[92m"
        RED = "\033[91m"
        END = "\033[0m"

    # Define nodes for tests
    root1 = Node(5, Node(2, None, Node(4)), Node(9, Node(9, None, Node(9)), Node(11)))

    root2 = None

    root3 = Node(1)

    root4 = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))

    root5 = Node(5, Node(3, Node(2, Node(1), None), Node(4)), None)

    root6 = Node(
        8,
        Node(6, Node(5, Node(2), Node(6)), Node(8, Node(8), Node(8))),
        Node(12, Node(10, Node(9), None), None),
    )

    tests = [
        (root1, 6, 5),
        (root1, 9, 9),
        (root1, 3, 2),
        (root1, 4, 4),
        (root2, 1, -math.inf),
        (root3, 1, 1),
        (root3, 2, 1),
        (root4, 5, 5),
        (root4, 8, 7),
        (root5, 1, 1),
        (root5, 5, 5),
        (root5, 6, 5),
        (root6, 9, 9),
        (root6, 13, 12),
        (root6, 1, 2),
        (root6, 8, 8),
        (root6, 6, 6),
        (root6, 7, 6),
        (root6, 11, 10),
        (root6, 4, 5),
    ]

    passed = 0

    print("Running Tests...\n")

    for i, (root, target, want) in enumerate(tests):
        got = find_closest(root, target)
        status = "✅ PASSED" if got == want else "❌ FAILED"
        color = Colors.GREEN if got == want else Colors.RED

        print(f"Test {i + 1}: {color}{status}{Colors.END}")
        print(f"  Input target      : {target}")
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
