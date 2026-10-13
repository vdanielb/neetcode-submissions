class MinStack:

    def __init__(self):
        self.currMin = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.currMin or val <= self.currMin[-1]:
            self.currMin.append(val)
            
    def pop(self) -> None:
        if self.currMin[-1] == self.stack[-1]:
            self.currMin.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currMin[-1]
