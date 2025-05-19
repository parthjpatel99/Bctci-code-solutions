def chess_moves(board, piece, r, c):
    def isValid(r, c):
        return 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] != 1
    
    res = []

    king_direction = [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    knight_direction = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [2, -1], [2, 1], [1, -2], [1, 2]]

    if piece == "knight":
        direction = knight_direction
    else:
        direction = king_direction

    for dir_r, dir_c in direction:
        new_r, new_c = r + dir_r, c + dir_c
        if piece == "queen":
            while isValid(new_r, new_c):
                res.append([new_r, new_c])
                new_r += dir_r
                new_c += dir_c
        elif isValid(new_r, new_c):
            res.append([new_r, new_c])
    
    return res

def run_tests():
    tests = [
        # Example 1 from the book - king moves
        ([[0, 0, 0, 1, 0, 0],
          [0, 1, 1, 1, 0, 0],
          [0, 1, 0, 1, 1, 0],
          [1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0]], "king", 3, 5,
            [[2, 5], [3, 4], [4, 4], [4, 5]]),
        # Example 2 from the book - knight moves
        ([[0, 0, 0, 1, 0, 0],
          [0, 1, 1, 1, 0, 0],
          [0, 1, 0, 1, 1, 0],
          [1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0]], "knight", 4, 3,
         [[2, 2], [3, 5], [5, 5]]),
        # Example 3 from the book - queen moves
        ([[0, 0, 0, 1, 0, 0],
          [0, 1, 1, 1, 0, 0],
          [0, 1, 0, 1, 1, 0],
          [1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0]], "queen", 4, 4,
         [[3, 4], [3, 5], [4, 0], [4, 1], [4, 2], [4, 3], [4, 5],
          [5, 3], [5, 4], [5, 5]]),
        # Edge case - 1x1 board
        ([[0]], "queen", 0, 0, []),
        # Edge case - all occupied except current position
        ([[1, 1], [1, 0]], "knight", 1, 1, []),
    ]

    passed_count = 0

    for i, (board, piece, r, c, want) in enumerate(tests):
        got = chess_moves(board, piece, r, c)
        got.sort()
        want.sort()
        passed = got == want
        if passed:
            passed_count += 1
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"Test {i + 1}: {status}")
        print(f"  Input board: {board}")
        print(f"  Piece: {piece}, Position: ({r}, {c})")
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