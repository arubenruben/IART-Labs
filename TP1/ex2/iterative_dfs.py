from state import State
from operators import operators

if __name__ == '__main__':
    solutionFound = False
    fail = False
    currentDepth = 0

    while not solutionFound and fail is not True:
        currState = State()
        solution = [currState]
        stateQueue = [currState]

        while currState is not None:
            if currState.is_final_state():
                solutionFound = True
                break

            if currState.depth > currentDepth:
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
                fail = True
                break

            currState = stateQueue.pop(0)
            solution.append(currState)

        currentDepth = currentDepth + 1

    if solutionFound:
        print(len(solution))
