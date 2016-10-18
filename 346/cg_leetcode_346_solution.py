class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.s = size
        self.q = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.q.append(float(val))
        
        while len(self.q) > self.s:
            self.q.pop(0)
            
        sum = 0
        
        for x in self.q:
            sum += x
            
        return sum / len(self.q)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
