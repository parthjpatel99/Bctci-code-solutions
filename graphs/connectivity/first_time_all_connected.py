def first_time_all_connected(V, cables):
    def visit(graph, visited, node):
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                visit(graph, visited, nbr)

    def is_before(cable_index):
        graph = [[] for _ in range(V)]
        for i in range(cable_index + 1):
            node1, node2 = cables[i]
            graph[node1].append(node2)
            graph[node2].append(node1)
        visited = {0}
        visit(graph, visited, 0)
        return len(visited) < V

    l, r = 0, len(cables) - 1
    if is_before(r):
        return -1
    while r - l > 1:
        mid = l + (r - l) // 2
        if is_before(mid):
            l = mid
        else:
            r = mid
    return r


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    # Assumes x is not already in the UnionFind.
    def add(self, x):
        self.parent[x] = x
        self.size[x] = 1

    # Assumes x is already in the UnionFind.
    def find(self, x):
        root = self.parent[x]
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            self.parent[x], x = root, self.parent[x]
        return root

    # Assumes x and y are already in the UnionFind.
    def union(self, x, y):
        repr_x, repr_y = self.find(x), self.find(y)
        if repr_x == repr_y:
            return  # They are already in the same set.
        if self.size[repr_x] < self.size[repr_y]:
            self.size[repr_y] += self.size[repr_x]
            self.parent[repr_x] = repr_y
        else:
            self.size[repr_x] += self.size[repr_y]
            self.parent[repr_y] = repr_x


def first_time_all_connected_union_find(V, cables):
    uf = UnionFind()
    for x in range(V):
        uf.add(x)
    groups = V
    for i in range(len(cables)):
        x, y = cables[i]

        # If x and y are not in the same group yet, union their groups.
        if uf.find(x) != uf.find(y):
            uf.union(x, y)
            groups -= 1
            if groups == 1:
                return i
    return -1


def run_tests():
    tests = [
        # Case from picture - becomes connected after cables[2].
        ("Case from picture", 4, [(0, 2), (1, 3), (0, 1), (1, 2)], 2),
        # Edge case - never gets fully connected
        ("Never connected", 3, [(0, 1)], -1),
        # Edge case - gets connected with final cable
        ("Connected at last", 3, [(0, 1), (1, 2)], 1),
        # Larger test case
        ("Larger case", 5, [(0, 1), (2, 3), (1, 2), (3, 4), (0, 4)], 3),
        # Edge case - redundant cables don't affect result
        ("Redundant edges", 4, [(0, 1), (1, 2), (2, 0), (2, 3), (3, 0)], 3),
        # No edges added
        ("No edges", 4, [], -1),
        # One edge added
        ("One edge only", 4, [(0, 1)], -1),
    ]

    passed, failed = 0, 0

    for i, (desc, V, cables, want) in enumerate(tests, 1):
        print(f"Test {i}: {desc}")

        got1 = first_time_all_connected(V, cables)
        got2 = first_time_all_connected_union_find(V, cables)

        ok1 = got1 == want
        ok2 = got2 == want

        if ok1 and ok2:
            print(f"  ✅ PASSED (Both Implementations)")
            passed += 1
        else:
            print(f"  ❌ FAILED")
            print(f"    Inputs: V={V}, cables={cables}")
            print(f"    Expected: {want}")
            if not ok1:
                print(f"    Got (DFS): {got1}")
            if not ok2:
                print(f"    Got (Union-Find): {got2}")
            failed += 1
        print("-" * 60)

    print("SUMMARY")
    print(f"  Total Tests: {len(tests)}")
    print(f"  ✅ Passed: {passed}")
    print(f"  ❌ Failed: {failed}")


run_tests()
