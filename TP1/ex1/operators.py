from state import State


def fill1(state):
    if state.cap_current_1 < state.cap_total_1:
        return State(state.cap_total_1, state.cap_current_2)


def fill2(state):
    if state.cap_current_2 < state.cap_total_2:
        return State(state.cap_current_1, state.cap_total_2)


def empty1(state):
    if state.cap_current_1 > 0:
        return State(0, state.cap_current_2)


def empty2(state):
    if state.cap_current_2 > 0:
        return State(state.cap_current_1, 0)


# Until Bucket 1 becomes empty
def pour12a(state):
    if state.cap_current_1 > 0 and state.cap_current_2 < state.cap_total_2 and state.cap_current_1 <= (
            state.cap_total_2 - state.cap_current_2):
        return State(0, state.cap_current_1 + state.cap_current_2)


# Until Bucket2 becomes full
def pour12b(state):
    if state.cap_current_1 > 0 and state.cap_current_2 < state.cap_total_2 and state.cap_current_1 >= (
            state.cap_total_2 - state.cap_current_2):
        return State(state.cap_current_1 - (state.cap_total_2 - state.cap_current_2), state.cap_total_2)


# Until Bucket2 becomes empty

def pour21a(state):
    if state.cap_current_2 > 0 and state.cap_current_1 < state.cap_total_1 and state.cap_current_2 <= (
            state.cap_total_1 - state.cap_current_1):
        return State(state.cap_current_1 + state.cap_current_2, 0)


# Until Bucket1 becomes full
def pour21b(state):
    if state.cap_current_2 > 0 and state.cap_current_1 < state.cap_total_1 and state.cap_current_2 >= (
            state.cap_total_1 - state.cap_current_1):
        return State(state.cap_total_1, state.cap_current_2 - (state.cap_total_1 - state.cap_current_1))


operators = [fill1, fill2, empty1, empty2, pour12a, pour12b, pour21a, pour21b]
