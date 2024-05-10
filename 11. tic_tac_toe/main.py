import random
import time


board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def display_board(highlight=None):
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
                time.sleep(0.5)
                return
            else:
                print('Invalid move. Please choose an empty cell within the range.')
        except ValueError:
            print('Invalid input. Please enter a number')

def make_ai_move():
    time.sleep(1) # delay to simulate AI "thinking" time
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        if board[row][col] == ' ':
            board[row][col] = 'O'
            print("AI has made its move:")
            time.sleep(0.5) # delay before displaying the board
            return


def check_winner():
    for i, row in enumerate(board):
        if row[0] == row[1] == row[2] != ' ':
            return (i, 0), (i, 1), (i, 2)
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return (0, col), (1, col), (2, col)
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return (0, 0), (1, 1), (2, 2)
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return (0, 2), (1, 1), (2, 0)
    
    if all(cell != ' ' for row in board for cell in row):
        return 'Tie'
    
    return None

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
                print(f"Player {current_player} wins.")
                display_board(winner)
            break
        current_player = 'O' if current_player == 'X' else 'X'

play_game()