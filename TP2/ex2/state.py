class State:
    def __init__(self, board, empty_place_cords):
        self._board = board
        self._empty_place_cords = empty_place_cords
        self._board_size = len(board)
        self._parent = None
        self._depth = 0

    def is_final_state(self):
        counter = 0
        if self.board[0][0] != 0:
            return False

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != counter:
                    return False
                counter += 1
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
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] is not state.board[i][j]:
                    return False
        return True
