import tkinter as tk
from tkinter import messagebox


def check_winner(board):
    combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return board[combo[0]]

    if "" not in board:
        return "Draw"

    return None


def minimax(board, is_maximizing):
    result = check_winner(board)

    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif result == "Draw":
        return 0

    if is_maximizing:
        best_score = -999
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 999
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score


def robot_move():
    best_score = -999
    move = None

    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i

    if move is not None:
        board[move] = "O"
        buttons[move].config(text="O")

    end_game()


def player_move(i):
    if board[i] == "" and not game_over:
        board[i] = "X"
        buttons[i].config(text="X")

        if not end_game():
            root.after(300, robot_move)


def end_game():
    global game_over
    result = check_winner(board)

    if result:
        game_over = True

        if result == "Draw":
            messagebox.showinfo("Game Over", "It's a Draw!")
        else:
            messagebox.showinfo("Game Over", f"{result} Wins!")

        return True

    return False


def reset_game():
    global board, game_over
    board = [""] * 9
    game_over = False
    for button in buttons:
        button.config(text="")


# ---------- UI ----------

root = tk.Tk()
root.title("Tic Tac Toe - Smart AI")

window_width = 320
window_height = 380

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.resizable(False, False)

board = [""] * 9
game_over = False

buttons = []

for i in range(9):
    btn = tk.Button(root,
                    text="",
                    font=("Arial", 20),
                    width=4,
                    height=2,
                    command=lambda i=i: player_move(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

reset_btn = tk.Button(root,
                      text="Restart",
                      font=("Arial", 14),
                      command=reset_game)

reset_btn.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()