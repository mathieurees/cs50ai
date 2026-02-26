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
    actions = []
    row_count = 0
    for row in board:
        cell_count = 0
        for cell in row:
            if cell is EMPTY:
                actions.append((row_count, cell_count))
            cell_count += 1
        row_count += 1
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possible_actions = actions(board)
    print(possible_actions)
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
    print(diagonals)
    for line in rows + columns + diagonals:
        if len(set(line)) == 1:
            if line[0]:
                return line[0]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
