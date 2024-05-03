import random


board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def display_board():
    print("   0   1   2")

    print("  " + "---" * 3)

    for i, row in enumerate(board):
        print(f"{i} | {' | '.join(row)} |")
        print("  " + "---" * 3)

def make_move(player):
    while True:
        try:
            row = int(input(f'Player {player}, enter the row number (0, 1, or 2): '))
            col = int(input(f"Player {player}, enter the column number (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print('Invalid move. Please choose an empty cell within the range.')
        except ValueError:
            print('Invalid input. Please enter a number')

def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    if all(cell != ' ' for row in board for cell in row):
        return 'Tie'
    
    return None

def make_ai_move():
    row = random.randint(0, 2)
    col = random.randint(0, 2)

    if board[row][col] == ' ':
        board[row][col] = 'O'
        print("AI has made its move:")
    else:
        make_ai_move()


def play_game():
    current_player = 'X'
    while True:
        display_board()
        if current_player == 'X':
            make_move(current_player)
        else:
            make_ai_move()
        winner = check_winner()
        if winner:
            if winner == 'Tie':
                print("It's a tie.")
            else:
                print(f"Player {winner} wins.")
            break
        current_player = 'O' if current_player == 'X' else 'X'

play_game()