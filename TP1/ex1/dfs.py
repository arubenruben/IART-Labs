from state import State
from operators import operators

if __name__ == '__main__':
    currState = State(0, 0, 4, 3)

    solution = [currState]
    stateQueue = [currState]

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
                    stateQueue.insert(0, potential_state)

        if len(stateQueue) == 0:
            print("No solutions")
            break

        currState = stateQueue.pop(0)
        solution.append(currState)

    print(len(solution))
