import math

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

# Function to check if the game is a draw
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Alpha-Beta Pruning function to evaluate the best possible score
def alpha_beta(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return 1
    if winner == "O":
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"  # Player X's turn
                    eval = alpha_beta(board, depth + 1, alpha, beta, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:  # Beta cut-off
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"  # Player O's turn
                    eval = alpha_beta(board, depth + 1, alpha, beta, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:  # Alpha cut-off
                        break
        return min_eval

# Function to find the best move for player X (computer)
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"  # Computer makes a move
                score = alpha_beta(board, 0, -math.inf, math.inf, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Function to play the Tic Tac Toe game
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initial empty board
    current_player = "O"  # Human player starts as 'O'
    
    while True:
        print_board(board)
        
        if current_player == "O":
            try:
                row = int(input("Enter row (1, 2, or 3): ")) - 1
                col = int(input("Enter column (1, 2, or 3): ")) - 1
                if board[row][col] != " ":
                    print("Cell already taken. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Enter numbers between 1 and 3.")
                continue
        else:
            row, col = best_move(board)  # Computer (Player X) makes the move

        board[row][col] = current_player

        if check_winner(board) == current_player:
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "X" if current_player == "O" else "O"  # Alternate players

# Run the game
tic_tac_toe()
