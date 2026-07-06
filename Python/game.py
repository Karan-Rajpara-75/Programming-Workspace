import random

board = [' ' for _ in range(9)]

def print_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def check_winner(player):
    win_combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_draw():
    return ' ' not in board

def player_move():
    while True:
        move = int(input("Enter position (1-9): ")) - 1
        if board[move] == ' ':
            board[move] = 'X'
            break
        else:
            print("Position already taken!")

def computer_move():
    available = [i for i in range(9) if board[i] == ' ']
    move = random.choice(available)
    board[move] = 'O'

print("🎮 Welcome to Tic Tac Toe")
print_board()

while True:
    player_move()
    print_board()
    if check_winner('X'):
        print("🎉 You Win!")
        break
    if is_draw():
        print("😐 It's a Draw!")
        break

    computer_move()
    print("Computer Move:")
    print_board()
    if check_winner('O'):
        print("💻 Computer Wins!")
        break
