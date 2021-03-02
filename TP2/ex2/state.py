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
    def board(self):
        return self._board

    @board.setter
    def board(self, value):
        self._board = value

    @property
    def empty_place_cords(self):
        return self._empty_place_cords

    @empty_place_cords.setter
    def empty_place_cords(self, value):
        self._empty_place_cords = value

    @property
    def board_size(self):
        return self._board_size

    def __eq__(self, state):
        return self.board == state.board
