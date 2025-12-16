board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

def print_board():
    print("---------")
    for row in board:
        print("|", row[0], row[1], row[2], "|")
    print("---------")

def check_win(player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_full():
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

player = 'X'

while True:
    print_board()
    row = int(input(f"Player {player}, enter row (0-2): "))
    col = int(input(f"Player {player}, enter column (0-2): "))

    if board[row][col] == ' ':
        board[row][col] = player

        if check_win(player):
            print_board()
            print(f"Player {player} wins!")
            break
        elif is_full():
            print_board()
            print("It's a draw!")
            break
        else:
            player = 'O' if player == 'X' else 'X'
    else:
        print("Cell already filled. Try again.")
