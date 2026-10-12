class MinStack:

    def __init__(self):
        self.st = []
        self._min = []
        

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self._min) == 0:
            self._min.append(val)
        else:
            self._min.append(min(val, self._min[-1]))

    def pop(self) -> None:
        self.st.pop()
        self._min.pop()  

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self._min[-1]
        
