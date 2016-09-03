class Stack():
    def __init__(self):
        self.ls = []
    
    def push(self, x):
        self.ls.append(x)
    
    def pop(self):
        return self.ls.pop()
        
    def is_empty(self):
        return len(self.ls) == 0

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.instack = Stack()
        self.outstack = Stack()
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.instack.push(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        while not self.instack.is_empty():
            self.outstack.push(self.instack.pop())
            
        ret = self.outstack.pop()
        
        while not self.outstack.is_empty():
            self.instack.push(self.outstack.pop())
            
        return ret
        

    def peek(self):
        """
        :rtype: int
        """
        while not self.instack.is_empty():
            self.outstack.push(self.instack.pop())
            
        ret = self.outstack.pop()
        self.outstack.push(ret)
        
        while not self.outstack.is_empty():
            self.instack.push(self.outstack.pop())
            
        return ret

    def empty(self):
        """
        :rtype: bool
        """
        return self.instack.is_empty()