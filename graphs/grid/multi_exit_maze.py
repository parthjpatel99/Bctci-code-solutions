from collections import deque


def exit_distances(maze):

    Q = deque()
    distances = [[-1] * len(maze[0]) for _ in range(len(maze))]

    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == "O":
                Q.append((r, c))
                distances[r][c] = 0

    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while Q:
        r, c = Q.popleft()
        for dir_r, dir_c in directions:
            new_r = r + dir_r
            new_c = c + dir_c

            if 0 <= new_r < len(maze) and 0 <= new_c < len(maze[0]):
                if distances[new_r][new_c] == -1 and maze[new_r][new_c] != "X":
                    distances[new_r][new_c] = distances[r][c] + 1
                    Q.append((new_r, new_c))

    return distances


def print_grid(grid):
    """Pretty print for 2D list or maze rows"""
    if isinstance(grid[0], list):  # numeric grid
        return "\n".join(" ".join(f"{x:2}" for x in row) for row in grid)
    else:  # string rows
        return "\n".join(" ".join(row) for row in grid)


def run_tests():
    tests = [
        # Example from book
        (
            ["...X.O", "OX.X..", "...X..", ".X....", "XOX.XX"],
            [
                [1, 2, 3, -1, 1, 0],
                [0, -1, 4, -1, 2, 1],
                [1, 2, 3, -1, 3, 2],
                [2, -1, 4, 5, 4, 3],
                [-1, 0, -1, 6, -1, -1],
            ],
        ),
        # Single exit
        (["...", ".O.", "..."], [[2, 1, 2], [1, 0, 1], [2, 1, 2]]),
        # Multiple exits
        (["O.O", "...", "O.O"], [[0, 1, 0], [1, 2, 1], [0, 1, 0]]),
        # Walls blocking direct paths
        (["O.X.", "XX..", "...O"], [[0, 1, -1, 2], [-1, -1, 2, 1], [3, 2, 1, 0]]),
        # Single cell
        (["O"], [[0]]),
    ]

    passed, failed = 0, 0
    for i, (maze_rows, want) in enumerate(tests, 1):
        maze = [list(row) for row in maze_rows]
        got = exit_distances(maze)

        print(f"Test {i}:")
        print(print_grid(maze_rows))  # show maze nicely

        if got == want:
            print("  ✅ PASSED")
            passed += 1
        else:
            print("  ❌ FAILED")
            print("  Expected:\n" + print_grid(want))
            print("  Got:\n" + print_grid(got))
            failed += 1
        print("-" * 50)

    print("SUMMARY")
    print(f"  Total: {len(tests)} | ✅ Passed: {passed} | ❌ Failed: {failed}")


run_tests()
