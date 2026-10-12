class MinStack:

    def __init__(self):
        self.stack = []
        # map num : min

    def push(self, val: int) -> None:
        s = self.stack
        if not s:
            s.append([val, val])
        else:
            s.append([val, min(val, s[-1][1])])

    def pop(self) -> None:
        s = self.stack
        s.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
