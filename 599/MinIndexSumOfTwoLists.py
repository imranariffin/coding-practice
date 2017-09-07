import sys

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        s = set(list1) & set(list2)
        sums = {e: list1.index(e) + list2.index(e) for e in s}
        minsum = reduce(lambda a,b: a if a < b else b, sums.values())
        ret = filter(lambda x: sums[x] <= minsum, sums.keys())
        return ret
