class State:
    def __init__(self, cap_current_1, cap_current_2, cap_total_1=4, cap_total_2=3):
        self._cap_current_1 = cap_current_1
        self._cap_current_2 = cap_current_2
        self._cap_total_1 = cap_total_1
        self._cap_total_2 = cap_total_2
        self._parent = None
        self._depth = 0
        self._cost = 0

    def is_final_state(self):
        return self.cap_current_1 == (self.cap_total_1 / 2)

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, state):
        self._parent = state.parent

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, depth):
        self._depth = depth

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, operator):
        self._operator = operator

    @property
    def cap_total_1(self):
        return self._cap_total_1

    @property
    def cap_total_2(self):
        return self._cap_total_2

    @property
    def cap_current_1(self):
        return self._cap_current_1

    @cap_current_1.setter
    def cap_current_1(self, value):
        self._cap_current_1 = value

    @property
    def cap_current_2(self):
        return self._cap_current_2

    @cap_current_2.setter
    def cap_current_2(self, value):
        self._cap_current_2 = value

    def __eq__(self, state):
        return self.cap_current_1 == state.cap_current_1 and self.cap_current_2 == state.cap_current_2
