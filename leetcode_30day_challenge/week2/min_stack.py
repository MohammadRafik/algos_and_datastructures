class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_index = []
        self.list = []

    def push(self, x: int) -> None:
        self.list.append(x)
        if self.min_index == []:
            self.min_index.append(0)
        elif self.list[-1] < self.list[self.min_index[-1]]:
            self.min_index.append(len(self.list)-1)

    def pop(self) -> None:
        if len(self.list)-1 == self.min_index[-1]:
            self.min_index.pop()
            self.list.pop()
        else:
            self.list.pop()

    def top(self) -> int:
        if self.list:
            return self.list[-1]
        else:
            return None
        
    def getMin(self) -> int:
        if self.min_index and self.list:
            return self.list[self.min_index[-1]]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())


