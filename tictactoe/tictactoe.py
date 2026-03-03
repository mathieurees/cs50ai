"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        x_count += row.count("X")
        o_count += row.count("O")
    if x_count == o_count:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    row_count = 0
    for row in board:
        cell_count = 0
        for cell in row:
            if cell is EMPTY:
                actions.add((row_count, cell_count))
            cell_count += 1
        row_count += 1
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possible_actions = actions(board)
    if action not in possible_actions:
        raise Exception("Invalid action.")
    current_player = player(board)
    new_board = deepcopy(board)
    new_board[action[0]][action[1]] = current_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    rows = [[],[],[]]
    columns = [[],[],[]]
    diagonals = [[],[]]
    for i in range(3):
        for j in range(3):
            if i == j:
                diagonals[0] = diagonals[0] + [board[i][j]]
                diagonals[1] = diagonals[1] + [board[i][2-j]]
            rows[i] = rows[i] + [board[i][j]]
            columns[j] = columns[j] + [board[i][j]]
    for line in rows + columns + diagonals:
        if len(set(line)) == 1:
            if line[0]:
                return line[0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True 


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if not winner(board):
        return 0
    return -1


def find_max(board):
    if terminal(board):
        return utility(board)
    max_val = -math.inf
    for action in actions(board):
        max_val = max(max_val, find_min(result(board, action)))
    return max_val


def find_min(board):
    if terminal(board):
        return utility(board)
    min_val = math.inf
    for action in actions(board):
        min_val = min(min_val, find_max(result(board, action)))
    return min_val


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)
    best_action = [None, 0]
    for action in actions(board):
        if current_player == X:
            print("X")
            max_action_value = find_min(result(board, action)) 
            if max_action_value >= best_action[1]:
                best_action = [action, max_action_value]
        if current_player == O:
            print("0")
            min_action_value = find_max(result(board, action)) 
            if min_action_value <= best_action[1]:
                best_action = [action, min_action_value]
        print(best_action)
    return best_action[0]
