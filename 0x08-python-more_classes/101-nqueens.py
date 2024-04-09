#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, N, result):
    if col >= N:
        solution = []
        for i in range(N):
            row = ''
            for j in range(N):
                if board[i][j] == 1:
                    row += 'Q'
                else:
                    row += '.'
            solution.append(row)
        result.append(solution)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_n_queens_util(board, col + 1, N, result) or res
            board[i][col] = 0

    return res

def solve_n_queens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    result = []

    if not solve_n_queens_util(board, 0, N, result):
        print("No solution exists")
        sys.exit(1)

    for solution in result:
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    else:
        solve_n_queens(sys.argv[1])
