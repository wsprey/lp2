def solve_n_queens(n):
    def is_safe(row, col, cols, diag1, diag2):
        return not (cols[col] or diag1[row - col] or diag2[row + col])

    def backtrack(row, board, cols, diag1, diag2, solutions):
        if row == n:
            solutions.append([row[:] for row in board])
            return

        for col in range(n):
            if is_safe(row, col, cols, diag1, diag2):
                # Place queen
                board[row][col] = 'Q'
                cols[col] = diag1[row - col] = diag2[row + col] = True
                
                # Recurse to next row
                backtrack(row + 1, board, cols, diag1, diag2, solutions)
                
                # Backtrack (remove queen)
                board[row][col] = '.'
                cols[col] = diag1[row - col] = diag2[row + col] = False

    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)  # Top-left to bottom-right
    diag2 = [False] * (2 * n - 1)  # Top-right to bottom-left
    
    backtrack(0, board, cols, diag1, diag2, solutions)
    return solutions