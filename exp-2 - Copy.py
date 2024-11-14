# Initialize the size of the chessboard
N = 8

# Function to print the chessboard
def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n" + "-" * (2 * N - 1) + "\n")

# Function to check if a queen can be placed safely at (row, col)
def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

# Function to solve the N-Queens problem using backtracking
def solve_nqueens(board, col):
    # Base case: If all queens are placed, return True
    if col >= N:
        print_solution(board)
        return True
    
    # Try placing a queen in all rows in the current column
    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place queen
            res = solve_nqueens(board, col + 1) or res
            board[i][col] = 0  # Backtrack and remove queen
    
    return res

# Initialize the chessboard with zeros
board = [[0] * N for _ in range(N)]

# Solve the N-Queens problem and print all solutions
if not solve_nqueens(board, 0):
    print("No solution exists")
