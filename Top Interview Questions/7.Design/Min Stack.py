import sys


class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append((x, min(self.getMin(), x)))

    def pop(self):
        self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return sys.maxsize


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
print(minStack.top())
print(minStack.getMin())
