class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.s = size
        self.q = []
        self.sum = 0
        self.c = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.q.append(float(val))
        self.sum += self.q[-1]
        self.c += 1

        while len(self.q) > self.s:
            self.sum -= q[0]
            self.c -= 1
            self.q.pop(0)
            
        return self.sum / self.c

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
