def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_draw(board):
    return all([cell != " " for row in board for cell in row])

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter row (1, 2, or 3): ")) - 1
            col = int(input(f"Player {current_player}, enter column (1, 2, or 3): ")) - 1
            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers between 1 and 3.")
            continue

        board[row][col] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
