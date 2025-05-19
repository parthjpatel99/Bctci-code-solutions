def safe_cells(board):
    res = [[0] * len(board[0]) for _ in range(len(board))]

    def mark_cell_reachable(r, c):
        def isValid(r,c):
            return 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 0
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

        for dir_r, dir_c in directions:
            newR = r + dir_r
            newC = c + dir_c

            while isValid(newR, newC):
                res[newR][newC] = 1
                newR += dir_r
                newC += dir_c
    

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 1:
                res[r][c] = 1
                mark_cell_reachable(r, c)

    return res


def run_tests():
    tests = [
        # Regular case with queens
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]],
         [[1, 1, 1, 1],
          [1, 0, 1, 1],
          [1, 1, 0, 1],
          [1, 1, 1, 1]]),
        # Edge case - empty board
        ([], []),
        # Edge case - 1x1 board with queen
        ([[1]], [[1]]),
        # Edge case - 1x1 board without queen
        ([[0]], [[0]]),
        # Edge case - no queens
        ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),
    ]

    passed_count = 0

    for i, (board, want) in enumerate(tests):
        got = safe_cells(board)
        passed = got == want
        if passed:
            passed_count += 1
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"Test {i + 1}: {status}")
        print(f"  Input board: {board}")
        print(f"  Expected Output: {want}")
        print(f"  Actual Output:   {got}")
        print()

    total_tests = len(tests)
    failed_count = total_tests - passed_count
    print("====== SUMMARY ======")
    print(f"Total tests run: {total_tests}")
    print(f"✅ Passed: {passed_count}")
    print(f"❌ Failed: {failed_count}")

run_tests()