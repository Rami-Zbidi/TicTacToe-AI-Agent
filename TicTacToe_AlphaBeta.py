import math
import time

# Constants
X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns an empty 3x3 Tic Tac Toe board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = sum(row.count(X) for row in board)
    count_o = sum(row.count(O) for row in board)
    return X if count_x == count_o else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] != EMPTY:
        return -1
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(EMPTY not in row for row in board)

def score(board):
    """
    Returns the score of the board.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def alphabeta(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == O:
        v = math.inf
        best_action = None
        alpha = -math.inf
        for action in actions(board):
            new_board = result(board, action)
            s = min_value(new_board, alpha, math.inf)
            if s < v:
                v = s
                best_action = action
            alpha = max(alpha, v)

    return best_action

def max_value(board, alpha, beta):
    """
    Returns the highest possible value for the current player.
    """
    if terminal(board):
        return score(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        alpha = min(alpha, v)
        if alpha >= beta:
            break

    return v

def min_value(board, alpha, beta):
    """
    Returns the lowest possible value for the current player.
    """
    if terminal(board):
        return score(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        beta = max(beta, v)
        if alpha >= beta:
            break

    return v

def print_board(board):
    """
    Prints the Tic Tac Toe board.
    """
    print("-------------")
    for row in board:
        print("|", end="")
        for item in row:
            symbol = " " if item == EMPTY else item
            print(f" {symbol} |", end="")
        print("\n-------------")

def play(board):
    print("Computer is thinking...")
    time.sleep(2)
    return alphabeta(board)

def playXO():
    """
    Runs the Tic Tac Toe game with Minimax algorithm.
    """
    print("Welcome to Tic Tac Toe!")
    print("You are playing against the computer.")

    board = initial_state()
    print_board(board)

    while not terminal(board):
        if player(board) == X:
            i = int(input("Enter row number (0-2): "))
            j = int(input("Enter column number (0-2): "))
            action = (i, j)
            if (result(board, action) == -1):
                print(("Case is not empty."))
                i = int(input("Enter row number (0-2): "))
                j = int(input("Enter column number (0-2): "))
                action = (i, j)
        else:
            action = play(board)

        board = result(board, action)
        print_board(board)

    winner_player = winner(board)
    if winner_player is None:
        print("Game ended in a tie.")
    else:
        if (winner_player == X):
            print("Human has won the game!")
        else:
            print("Computer has won the game!")

if __name__ == "__main__":
    playXO()