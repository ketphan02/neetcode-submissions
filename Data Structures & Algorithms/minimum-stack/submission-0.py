class MinStack:

    def __init__(self):
        self.cur_min = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.cur_min) > 0:
            self.cur_min.append(min(self.cur_min[-1], val))
        else:
            self.cur_min.append(val)

    def pop(self) -> None:
        self.cur_min.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.cur_min[-1]
