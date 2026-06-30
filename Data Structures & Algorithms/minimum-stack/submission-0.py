class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(self.minimum, val)

    def pop(self) -> None:
        self.stack = self.stack[:len(self.stack) - 1]
        self.minimum = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
