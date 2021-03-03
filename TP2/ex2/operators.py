from state import State
from copy import deepcopy


def up(state):
    x, y = state.empty_place_cords

    if x == 0:
        return None

    new_board = deepcopy(state.board)

    new_board[x][y] = new_board[x - 1][y]
    new_board[x - 1][y] = 0

    return State(new_board, (x - 1, y))


def down(state):
    x, y = state.empty_place_cords

    if x == (state.board_size - 1):
        return None

    new_board = deepcopy(state.board)

    new_board[x][y] = new_board[x + 1][y]
    new_board[x + 1][y] = 0

    return State(new_board, (x + 1, y))


def left(state):
    x, y = state.empty_place_cords

    if y == 0:
        return None

    new_board = deepcopy(state.board)

    new_board[x][y] = new_board[x][y - 1]
    new_board[x][y - 1] = 0

    return State(new_board, (x, y - 1))


def right(state):
    x, y = state.empty_place_cords

    if y == (state.board_size - 1):
        return None

    new_board = deepcopy(state.board)

    new_board[x][y] = new_board[x][y + 1]
    new_board[x][y + 1] = 0

    return State(new_board, (x, y + 1))


operators = [up, right, left, down]
