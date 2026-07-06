import chess
import random

# Board evaluation values
piece_value = {
    chess.PAWN: 10,
    chess.KNIGHT: 30,
    chess.BISHOP: 30,
    chess.ROOK: 50,
    chess.QUEEN: 90,
    chess.KING: 900
}

def evaluate_board(board):
    score = 0
    for piece in piece_value:
        score += len(board.pieces(piece, chess.WHITE)) * piece_value[piece]
        score -= len(board.pieces(piece, chess.BLACK)) * piece_value[piece]
    return score

# EASY MODE (Random Move)
def easy_ai(board):
    return random.choice(list(board.legal_moves))

# MEDIUM MODE (Prefer Capture)
def medium_ai(board):
    captures = [m for m in board.legal_moves if board.is_capture(m)]
    return random.choice(captures) if captures else random.choice(list(board.legal_moves))

# HARD MODE (Minimax)
def minimax(board, depth, is_max):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    moves = list(board.legal_moves)
    if is_max:
        best = -9999
        for move in moves:
            board.push(move)
            best = max(best, minimax(board, depth - 1, False))
            board.pop()
        return best
    else:
        best = 9999
        for move in moves:
            board.push(move)
            best = min(best, minimax(board, depth - 1, True))
            board.pop()
        return best

def hard_ai(board):
    best_move = None
    best_value = -9999
    for move in board.legal_moves:
        board.push(move)
        value = minimax(board, 2, False)
        board.pop()
        if value > best_value:
            best_value = value
            best_move = move
    return best_move

# MAIN GAME
def play_game():
    board = chess.Board()
    print("Choose difficulty: easy / medium / hard")
    mode = input("Mode: ").lower()

    while not board.is_game_over():
        print(board)
        if board.turn == chess.WHITE:
            move = input("Your move (e2e4): ")
            try:
                board.push(chess.Move.from_uci(move))
            except:
                print("Invalid move")
        else:
            if mode == "easy":
                ai_move = easy_ai(board)
            elif mode == "medium":
                ai_move = medium_ai(board)
            else:
                ai_move = hard_ai(board)

            print("AI move:", ai_move)
            board.push(ai_move)

    print("Game Over")
    print(board.result())

if __name__ == "__main__":
    play_game() 