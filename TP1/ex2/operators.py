from state import State


def miss_l_to_right(state):
    if state.number_miss_left() > 0 and state.number_cannibals_left() - 1 >= state.number_cannibals_left() and state.boat_position == "left":
        print("miss_l_to_right")
        return State(state.number_miss_right + 1, state.number_cannibals_right, "right")


def cann_l_to_right(state):
    if state.number_cannibals_left() > 0 and state.number_miss_right >= state.number_cannibals_right + 1 and state.boat_position == "left":
        print("cann_l_to_right")
        return State(state.number_miss_right, state.number_cannibals_right + 1, "right")


def miss_miss_l_to_right(state):
    if state.number_miss_left() >= 2 and state.number_miss_left() - 2 >= state.number_cannibals_left() and state.boat_position == "left":
        print("miss_miss_l_to_right")
        return State(state.number_miss_right + 2, state.number_cannibals_right, "right")


def cann_cann_l_to_right(state):
    if state.number_cannibals_left() >= 2 and state.number_miss_right >= state.number_cannibals_right + 2 and state.boat_position == "left":
        print("cann_cann_l_to_right")
        return State(state.number_miss_right, state.number_cannibals_right + 2, "right")


def miss_cann_l_to_right(state):
    if state.number_miss_left() > 0 and state.number_miss_left() > 0 and state.boat_position == "left":
        print("miss_cann_l_to_right")
        return State(state.number_miss_right + 1, state.number_cannibals_right + 1, "right")


def cann_r_to_left(state):
    if state.number_cannibals_right > 0 and state.number_miss_left() >= state.number_cannibals_left() + 1 and state.boat_position == "right":
        print("cann_r_to_left")
        return State(state.number_miss_right, state.number_cannibals_right - 1, "left")


def miss_miss_r_to_left(state):
    if state.number_miss_right >= 2 and state.number_miss_right - 2 >= state.number_cannibals_right and state.boat_position == "right":
        print("miss_miss_r_to_left")
        return State(state.number_miss_right - 2, state.number_cannibals_right, "left")


def miss_r_to_left(state):
    if state.number_miss_right > 0 and state.number_miss_right - 1 >= state.number_cannibals_right and state.boat_position == "right":
        print("miss_r_to_left")
        return State(state.number_miss_right - 1, state.number_cannibals_right, "left")


def cann_cann_r_to_left(state):
    if state.number_cannibals_right >= 2 and state.number_miss_left() >= state.number_cannibals_left() + 2 and state.boat_position == "right":
        print("cann_cann_r_to_left")
        return State(state.number_miss_right, state.number_cannibals_right - 2, "left")


def miss_cann_r_to_left(state):
    if state.number_miss_right > 0 and state.number_cannibals_right > 0 and state.boat_position == "right":
        print("miss_cann_r_to_left")
        return State(state.number_miss_right - 1, state.number_cannibals_right - 1, "left")


operators = [
    cann_r_to_left,
    miss_cann_r_to_left,
    cann_cann_r_to_left,
    miss_r_to_left,
    miss_miss_r_to_left,
    cann_l_to_right,
    miss_cann_l_to_right,
    cann_cann_l_to_right,
    miss_l_to_right,
    miss_miss_l_to_right,
]
