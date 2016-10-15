# Based on charles8135's solution.
# Refer <https://discuss.leetcode.com/topic/11985/my-python-solution>.
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.L = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        currMin = self.getMin()
        
        if currMin == None or x < currMin:
            currMin = x
            
        self.L.append((x, currMin))

    def pop(self):
        """
        :rtype: void
        """
        self.L.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.L) < 1:
            return None
            
        return self.L[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.L) < 1:
            return None
            
        return self.L[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
