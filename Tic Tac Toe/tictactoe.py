# print board
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


# select first player
def select_first_player():
    player_1 = 'O'
    player_2 = 'X'
    print(f"Player #1: {player_1}  Player #2: {player_2}")

    current_player = input("Player 1--(O) or 2--(X)?\nEnter your choice for first move: ")
    while current_player not in ['1', '2']:
        current_player = input("Invalid choice! Please enter 1 or 2: ")

    return player_1 if current_player == '1' else player_2


# take input from player
def get_move():
    row = int(input("Enter row number 0-2: "))
    col = int(input("Enter col number 0-2: "))
    while row < 0 or row > 2 or col < 0 or col > 2:
        row = int(input("Enter row number 0-2: "))
        col = int(input("Enter col number 0-2: "))
    return (row, col)


# check win or tie
def check_win_or_draw(board, move, current_player):
    row, col = move
    if board[row][col] == '-':
        board[row][col] = current_player
        print_board(board)

        if is_win(board, current_player):
            return "win"
        if is_draw(board):
            return "draw"


# check for win
def is_win(board, current_player):
    diagonal_count = 0
    inv_diagonal_count = 0

    for i in range(len(board)):
        row_count = 0
        col_count = 0
        for j in range(len(board)):
            if board[i][j] == current_player:  # row
                row_count += 1
            if board[j][i] == current_player:  # col
                col_count += 1
            if i == j and board[i][j] == current_player:  # main diagonal
                diagonal_count += 1
            if i + j == len(board) - 1 and board[i][j] == current_player:  # anti-diagonal
                inv_diagonal_count += 1

        if row_count == 3 or col_count == 3:
            return True

    return diagonal_count == 3 or inv_diagonal_count == 3


# check for draw
def is_draw(board):
    return all(cell != '-' for row in board for cell in row)


# switch player
def switch_player(current_player):
    return 'O' if current_player == 'X' else 'X'


def main():
    curr_player = select_first_player()
    print_board(board)

    for _ in range(9):
        move = get_move()
        status = check_win_or_draw(board, move, curr_player)

        if status == "win":
            print(f"{curr_player} wins!")
            break
        elif status == "draw":
            print("It's a draw!")
            break

        curr_player = switch_player(curr_player)
    else:
        print("It's a draw!")  # if loop finishes with no break

main()        
