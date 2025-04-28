def solve_n_queens(n):
    def is_safe(row, col, cols, diag1, diag2):
        return not (cols[col] or diag1[row - col] or diag2[row + col])

    def backtrack(row, board, cols, diag1, diag2, solutions):
        if row == n:
            solutions.append([row[:] for row in board])
            return

        for col in range(n):
            if is_safe(row, col, cols, diag1, diag2):
                board[row][col] = 'Q'
                cols[col] = diag1[row - col] = diag2[row + col] = True
                backtrack(row + 1, board, cols, diag1, diag2, solutions)
                board[row][col] = '.'
                cols[col] = diag1[row - col] = diag2[row + col] = False

    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)
    backtrack(0, board, cols, diag1, diag2, solutions)
    return solutions

def print_solution(solution):
    for row in solution:
        print(' '.join(row))
    print()

def main_n_queens():
    print("N-Queens Solver (Branch and Bound)")
    n = int(input("Enter board size (n): "))
    solutions = solve_n_queens(n)
    print(f"\nFound {len(solutions)} solutions:")
    for i, sol in enumerate(solutions, 1):
        print(f"Solution {i}:")
        print_solution(sol)

if __name__ == "__main__":
    main_n_queens()