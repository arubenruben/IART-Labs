class State:
    def __init__(self, board, empty_place_cords):
        self._board = board
        self._empty_place_cords = empty_place_cords
        self._board_size = len(board)
        self._parent = None
        self._depth = 0

    def is_final_state(self):
        expected_value = 1

        for row in self.board:
            for cell in row:
                if expected_value == (self.board_size * self.board_size):
                    expected_value = 0

                if cell != expected_value:
                    return False

                expected_value += 1

        return True

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, state):
        self._parent = state
        self._depth = state.depth

    @property
    def board(self):
        return self._board

    @property
    def empty_place_cords(self):
        return self._empty_place_cords

    @empty_place_cords.setter
    def empty_place_cords(self, value):
        self._empty_place_cords = value

    @property
    def board_size(self):
        return self._board_size

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = value

    def get_g(self):
        return self.depth

    def get_h(self):
        counter = 0

        for i in range(self._board_size):
            for j in range(self._board_size):
                value = self._board[i][j]

                expected_row = (value - 1) / self._board_size
                expected_col = (value - 1) % self._board_size

                counter += (abs(expected_row - i) + abs(expected_col - j))

        return counter


def __eq__(self, state):
    return self.board == state.board


def get_a_star_value(state):
    return state.get_h() + state.get_g()


def get_greedy_value(state):
    return state.get_h()


def get_uniform_cost_value(state):
    return state.get_g()
