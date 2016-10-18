class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        tMinus10 = timestamp - 10
        
        while len(self.q) > 0 and self.q[0][0] <= tMinus10:
            self.q.pop(0)
            
        res = True
        
        for item in self.q:
            if item[1] == message:
                res = False
                
        if res:
            self.q.append((timestamp, message))
            
        return res

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)