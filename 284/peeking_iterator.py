# # Below is the interface for Iterator, which is already defined for you.
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#         self.ls = nums

#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#         return len(self.ls) > 0

#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
#         return self.ls.pop(0)

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.head = None
        self.has_next = self.iter.hasNext()
        if self.has_next:
            self.head = self.iter.next()


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.head

    def next(self):
        """
        :rtype: int
        """
        ret = self.head
        self.has_next = self.iter.hasNext()
        if self.has_next:
            self.head = self.iter.next()
        else:
            self.head = None
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has_next
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

if __name__=="__main__":
    # pit = PeekingIterator(Iterator([x for x in range(10)]))
    nums = [x for x in range(10)]
    nums = []
    it = Iterator([x for x in nums])
    # it = Iterator([1])
    pit = PeekingIterator(it)

    # print it.ls
    # while it.hasNext():
    #     print it.next(), 

    print nums
    while pit.hasNext():
        print pit.next(),