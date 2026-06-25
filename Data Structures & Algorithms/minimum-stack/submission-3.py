class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1:
            self.minimum = val
        self.minimum = min(self.minimum, val)

    def pop(self) -> None:
        self.stack = self.stack[:len(self.stack) - 1]
        
        if self.minimum != None and self.stack:
            self.minimum = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
