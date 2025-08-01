class Node:
    def __init__(self, kind, num, children):
        self.kind = kind
        self.num = num
        self.children = children


def evaluate(node):
    if node.kind == "num":
        return node.num

    children_evals = []
    for child in node.children:
        children_evals.append(evaluate(child))

    if node.kind == "product":
        return product(children_evals)
    elif node.kind == "sum":
        return sum(children_evals)
    elif node.kind == "max":
        return max(children_evals)
    else:
        return min(children_evals)
    raise ValueError("Invalid kind")


def product(vals):
    res = 1
    for val in vals:
        res *= val
    return res


def run_tests():
    tests = [
        # Test 0: Example from the book
        (
            Node(
                "min",
                None,
                [
                    Node(
                        "max",
                        None,
                        [
                            Node("num", 4, None),
                            Node("num", 6, None),
                            Node(
                                "sum",
                                None,
                                [Node("num", 5, None), Node("num", 7, None)],
                            ),
                        ],
                    ),
                    Node(
                        "sum",
                        None,
                        [
                            Node(
                                "product",
                                None,
                                [Node("num", 6, None), Node("num", 8, None)],
                            )
                        ],
                    ),
                ],
            ),
            12,
        ),
        # Test 1: (2 + 3) * 4 = 20
        (
            Node(
                "product",
                None,
                [
                    Node("sum", None, [Node("num", 2, None), Node("num", 3, None)]),
                    Node("num", 4, None),
                ],
            ),
            20,
        ),
        # Test 2: Single number
        (Node("num", 5, None), 5),
        # Test 3: Empty sum node
        (Node("sum", None, []), 0),
        # Test 4: Empty product node
        (Node("product", None, []), 1),
        # Test 5: min(2, max(3, 4)) + product(1,2,3) = 2 + 6 = 8
        (
            Node(
                "sum",
                None,
                [
                    Node(
                        "min",
                        None,
                        [
                            Node("num", 2, None),
                            Node(
                                "max",
                                None,
                                [Node("num", 3, None), Node("num", 4, None)],
                            ),
                        ],
                    ),
                    Node(
                        "product",
                        None,
                        [
                            Node("num", 1, None),
                            Node("num", 2, None),
                            Node("num", 3, None),
                        ],
                    ),
                ],
            ),
            8,
        ),
        # Subexpression tests
        # max(4, 6, sum(5+7)) = max(4, 6, 12) = 12
        (
            Node(
                "max",
                None,
                [
                    Node("num", 4, None),
                    Node("num", 6, None),
                    Node("sum", None, [Node("num", 5, None), Node("num", 7, None)]),
                ],
            ),
            12,
        ),
        # sum(product(6, 8)) = sum(48) = 48
        (
            Node(
                "sum",
                None,
                [Node("product", None, [Node("num", 6, None), Node("num", 8, None)])],
            ),
            48,
        ),
    ]

    passed = 0
    failed = 0
    print("🧪 Running Tests for evaluate(Node)...\n")

    for i, (root, want) in enumerate(tests, 1):
        got = evaluate(root)
        if got == want:
            status = "✅ PASSED"
            passed += 1
        else:
            status = "❌ FAILED"
            failed += 1
        label = root.kind if root else "None"
        print(f"Test {i}: {status}")
        print(f"  Root Kind: {label}")
        print(f"  Expected : {want}")
        print(f"  Got      : {got}\n")

    print("📊 Summary")
    print(f"  Total : {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")


run_tests()
