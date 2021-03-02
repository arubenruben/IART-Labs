class State:

    def __init__(self, number_miss_right=3, number_cannibals_right=3, boat_position="right"):
        self._number_miss_right = number_miss_right
        self._number_cannibals_right = number_cannibals_right
        self._boat_position = boat_position
        self._parent = None
        self._depth = 0

    def is_final_state(self):
        return self._number_miss_right == 0 and self._number_cannibals_right == 0

    @property
    def boat_position(self):
        return self._boat_position

    @boat_position.setter
    def boat_position(self, value):
        self._boat_position = value

    @property
    def number_miss_right(self):
        return self._number_miss_right

    @number_miss_right.setter
    def number_miss_right(self, value):
        self._number_miss_right = value

    @property
    def number_cannibals_right(self):
        return self._number_cannibals_right

    @number_cannibals_right.setter
    def number_cannibals_right(self, value):
        self._number_miss_right = value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, state):
        self._parent = state
        self._depth = state.depth + 1

    def number_cannibals_left(self):
        return 3 - self._number_cannibals_right

    def number_miss_left(self):
        if 3 - self._number_miss_right == 0:
            return 999999999999999999

        return 3 - self._number_miss_right

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = value

    def __eq__(self, state):
        return self.number_cannibals_right == state.number_cannibals_right \
               and state.number_miss_right == self.number_miss_right and self.boat_position == state.boat_position
