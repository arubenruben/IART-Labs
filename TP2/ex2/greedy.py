from board_factory import create_board
from operators import operators
from state import *

if __name__ == '__main__':

    startingInfo = create_board(1)
    currState = State(startingInfo[0], startingInfo[1])

    stateQueue = [currState]
    solution = []

    while currState is not None:
        if currState.is_final_state():
            break

        for operator in operators:
            potential_state = operator(currState)

            if potential_state is not None:
                unique = True

                for alreadyVisited in solution:
                    if alreadyVisited == potential_state:
                        unique = False
                if unique:
                    potential_state.parent = currState
                    stateQueue.append(potential_state)
                    stateQueue.sort(key=get_greedy_value)

        if len(stateQueue) == 0:
            print("No solutions")
            break

        currState = stateQueue.pop(0)
        solution.append(currState)

    state = solution.pop()
    print(state.board)
