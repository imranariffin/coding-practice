class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.L = []
        self.minElement = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.L.append(x)
        
        if self.minElement == None or x < self.minElement:
            self.minElement = x

    def pop(self):
        """
        :rtype: void
        """
        x = self.L.pop()
        
        if len(self.L) < 1:
            self.minElement = None
            return
        
        sortedL = sorted(self.L)
        self.minElement = sortedL[0]

    def top(self):
        """
        :rtype: int
        """
        return self.L[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minElement


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
