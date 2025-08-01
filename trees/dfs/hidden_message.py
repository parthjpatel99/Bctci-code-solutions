class Node:
    def __init__(self, text, left=None, right=None):
        self.text = text
        self.left = left
        self.right = right


def hidden_message(root):
    res = []

    def dfs(node):
        if not node:
            return
        if node.text[0] == "b":
            res.append(node.text[1])
            dfs(node.left)
            dfs(node.right)
        elif node.text[0] == "i":
            dfs(node.left)
            res.append(node.text[1])
            dfs(node.right)
        else:
            dfs(node.left)
            dfs(node.right)
            res.append(node.text[1])

    dfs(root)
    return "".join(res)


def run_tests():
    # Constructing the trees
    root1 = Node("bn")
    root1.left = Node("i_")
    root1.left.left = Node("ae")
    root1.left.right = Node("it")
    root1.left.left.left = Node("bi")
    root1.left.left.right = Node("bc")
    root1.right = Node("a!")
    root1.right.left = Node("br")
    root1.right.right = Node("ay")

    root2 = None
    root3 = Node("bx")
    root4 = Node("ix")
    root5 = Node("ax")

    root6 = Node(
        "b1", Node("b2", Node("b4"), Node("b5")), Node("b3", Node("b6"), Node("b7"))
    )

    root7 = Node(
        "i1", Node("i2", Node("i4"), Node("i5")), Node("i3", Node("i6"), Node("i7"))
    )

    root8 = Node(
        "a1", Node("a2", Node("a4"), Node("a5")), Node("a3", Node("a6"), Node("a7"))
    )

    root9 = Node("bh", Node("be", Node("bl"), Node("il")), Node("ao"))

    root10 = Node("cx")
    root11 = Node("i")
    root12 = Node("bxy")

    # Test cases (excluding the invalid ones not part of `hidden_message`)
    tests = [
        (root1, "nice_try!"),  # Example from book
        (root2, ""),  # Empty tree
        (root3, "x"),  # Single TreeNode before
        (root4, "x"),  # Single TreeNode in
        (root5, "x"),  # Single TreeNode after
        (root6, "1245367"),  # All before order
        (root7, "4251637"),  # All in order
        (root8, "4526731"),  # All after order
        (root9, "hello"),  # Mixed orders spelling "hello"
    ]

    passed = 0
    failed = 0

    print("🔍 Running Hidden Message Tree Tests...\n")

    for i, (root, expected) in enumerate(tests, 1):
        result = hidden_message(root)
        status = "✅ PASSED" if result == expected else "❌ FAILED"
        if result == expected:
            passed += 1
        else:
            failed += 1

        root_label = root.text if root else "None"

        print(f"Test {i}: {status}")
        print(f"  Root:      {root_label}")
        print(f"  Expected:  {expected}")
        print(f"  Got:       {result}")
        print()

    print("📊 Summary")
    print(f"  Total:  {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")


run_tests()
