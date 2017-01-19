# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        ret = 0
        for nls in nestedList:
            ret += self.__depthSum__(nls, 1)
        return ret
        
    def __depthSum__(self, nls, depth):
        """
        :type nestedList: NestedList
        :rtype: int
        """
        if nls.isInteger():
            return depth * nls.getInteger()
            
        ls = nls.getList()
        ret = 0
        for nls in ls:
            ret += self.__depthSum__(nls, depth+1)
    
        return ret