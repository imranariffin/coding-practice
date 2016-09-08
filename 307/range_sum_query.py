# Solution 1: too slow to pass leetcode
# import math

# class SegmentNode(object):
#     def __init__(self, val, noderange):
#         """
#         range is tuple. if empty, isleaf = true
#         """
#         self.val = val
#         self.range = noderange
#         self.isleaf = False
#         if self.range[0] == self.range[1]:
#             self.isleaf = True

#     def __str__(self):
#         return "N({}, {})".format(self.val, self.range)

# class SegmentTree(object):
#     def __init__(self, ls):
#         n = len(ls)
#         if n == 0:
#             self.tree_arr = []
#             return
#         # height of the tree
#         h = int(math.ceil(math.log(n, 2)))
#         # max size of segment tree
#         max_size = 2*int(math.pow(2, h))-1

#         # print max_size
#         self.max_size = max_size
#         self.h = h
#         self.tree_arr = [None for x in range(max_size)]
#         self.tree_arr[0] = self.__create_st__(ls, 0, n-1, 0)

#     def get_mid(self, start, end):
#         return start+(end-start)/2

#     def __create_st__(self, ls, start, end, i):
#         # reached at leaf ie outer node
#         if start == end:
#             node = SegmentNode(ls[start], (start, end))
#             self.tree_arr[i] = node
#             # return ls[start]
#             return node

#         # each inner node has two children
#         # get the sum of its children
#         mid = self.get_mid(start, end)

#         self.tree_arr[i] = SegmentNode(\
#             self.__create_st__(ls, start, mid, 2*i+1).val + \
#             self.__create_st__(ls, mid+1, end, 2*i+2).val, \
#             (start, end))
#         return self.tree_arr[i]

#     def __find_node__(self, i, k):
#         node = self.tree_arr[k]
#         mid = self.get_mid(node.range[0], node.range[1])

#         # print node.val, "({},{}), i={}, mid={}".format(node.range[0], node.range[1], i, mid)

#         if node.isleaf:
#             return node.val

#         if i <= mid:
#             return self.__find_node__(i, 2*k+1)
#         return self.__find_node__(i, 2*k+2)

#     def find_node(self, i):
#         return self.__find_node__(i, 0)

#     def __get_sum_range__(self, i, j, k):
#         node = self.tree_arr[k]
#         leftbound = node.range[0]
#         rightbound = node.range[1]
#         mid = self.get_mid(leftbound, rightbound)

#         if i == j:
#             return self.find_node(i)

#         # print "at", k, node, "searching for ({}, {})".format(i, j)

#         if node.isleaf:
#             return node.val

#         if i < leftbound or j > rightbound:
#             assert(False)

#         if i >= leftbound and i <= mid and j <= rightbound and j > mid:
#             # print "CASE I"
#             return self.__get_sum_range__(i, mid, 2*k+1) + \
#             self.__get_sum_range__(mid+1, j, 2*k+2)

#         if i < leftbound and j < mid:
#             # print "CASE II"
#             return self.__get_sum_range__(leftbound, j, 2*k+1)

#         if i > mid and j > rightbound:
#             # print "CASE III"
#             return self.__get_sum_range__(i, rightbound, 2*k+2)

#         if i < leftbound and j < rightbound:
#             # print "CASE IV"
#             return self.__get_sum_range__(leftbound, mid, 2*k+1) + \
#             self.__get_sum_range__(mid+1, rightbound, 2*k+2)

#         if i >= leftbound and j <= mid:
#             # print "CASE V"
#             return self.__get_sum_range__(i, j, 2*k+1)
#         if i > mid and j <= rightbound:
#             # print "CASE VI"
#             return self.__get_sum_range__(i, j, 2*k+2)

#         # print "searching for", (i, j), "at ", (leftbound, mid, rightbound)
#         # print "is leaf?", node.isleaf
#         assert(False)

#     def get_sum_range(self, i, j):
#         return self.__get_sum_range__(i, j, 0)

#     def __update_st__(self, i, diff, k):
#         node = self.tree_arr[k]
#         mid = self.get_mid(node.range[0], node.range[1])

#         node.val += diff

#         if node.isleaf:
#             return

#         if i <= mid:
#             self.__update_st__(i, diff, 2*k+1)
#             return
#         self.__update_st__(i, diff, 2*k+2)

#     def update_st(self, i, val):
#         diff = val-self.find_node(i)
#         self.__update_st__(i, diff, 0)

# class NumArray(object):
#     def __init__(self, nums):
#         """
#         initialize your data structure here.
#         :type nums: List[int]
#         """
#         self.st = SegmentTree(nums)        

#     def update(self, i, val):
#         """
#         :type i: int
#         :type val: int
#         :rtype: int
#         """
#         self.st.update_st(i, val)


#     def sumRange(self, i, j):
#         """
#         sum of elements nums[i..j], inclusive.
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         return self.st.get_sum_range(i, j)

# # Your NumArray object will be instantiated and called as such:
# # numArray = NumArray(nums)
# # numArray.sumRange(0, 1)
# # numArray.update(1, 10)
# # numArray.sumRange(1, 2)

# def test_create_st():
#     print "=============="
#     print "test_create_st:"
#     print "=============="
#     ls = [1,2,3]
#     print ls
#     st = SegmentTree(ls)
#     print [n.__str__() for n in st.tree_arr]
#     print " --- "
#     ls = [-1, -2, -3]
#     print ls
#     st = SegmentTree(ls)
#     print [n.__str__() for n in st.tree_arr]
#     print " --- "
#     ls = [x for x in range(12)]
#     print ls
#     st = SegmentTree(ls)
#     print [n.__str__() for n in st.tree_arr]
#     print " --- "
#     ls = [x if x%2==0 else -x for x in range(9)]
#     print ls
#     st = SegmentTree(ls)
#     print [n.__str__() for n in st.tree_arr]
#     print " --- "    

# def test_update():
#     print "=============="
#     print "test_update:"
#     print "=============="
#     # N = NumArray()
#     ls = [1,2,3,4,5]
#     print ls
#     st = SegmentTree(ls)
#     print [n.__str__() for n in st.tree_arr]
#     # for i in range(len(ls)):
#     #     # print "getvalue({}):".format(i), st.get_leaf_value(i)
#     #     print "st.__get_sum_range__({}, 0, 0):\n".format(i), st.__get_sum_range__(i, 0, 0)

#     # print st.find_node(4)
#     print "st.get_sum_range(0, 0)"
#     print st.get_sum_range(0, 0)
#     print st.get_sum_range(0, 1)
#     print st.get_sum_range(0, 4)
#     print st.get_sum_range(2, 2)
#     # print st.find

#     print [n.__str__() for n in st.tree_arr]
#     st.update_st(0, 5)
#     print [n.__str__() for n in st.tree_arr]

# if __name__=="__main__":
#     test_create_st()
#     test_update()

# # Solution 2: also too slow
# import math
# class NumArray(object):
#     def __init__(self, nums):
#         """
#         initialize your data structure here.
#         :type nums: List[int]
#         """
#         n = len(nums)

#         if n <= 0:
#             self.st = []
#             self.arr = []
#             return

#         h = int(math.ceil(math.log(n, 2)))
#         max_size = 2*int(math.pow(2, h))-1

#         self.st = [0 for x in range(max_size)]
#         self.arr = [x for x in nums]

#         self.construct_segment_tree(nums, 0, n-1, 0)

#     def get_mid(self, i, j):
#         return i+(j-i)/2

#     def construct_segment_tree(self, nums, i, j, k):

#         if i == j:
#             ret = nums[i]
#             self.st[k] = ret
#             return self.st[k]

#         mid = self.get_mid(i, j)

#         print self.arr
#         print self.st
#         print (i, mid, j), k

#         self.st[k] = self.construct_segment_tree(nums, i, mid, 2*k+1) + \
#         self.construct_segment_tree(nums, mid+1, j, 2*k+2)

#         return self.st[k]

#     def __update__(self, i, j, k, diff, ii):
#         if k < i or k > j:
#             return

#         self.st[ii] += diff
#         if i != j:
#             mid = self.get_mid(i, j)
#             self.__update__(i, mid, k, diff, 2*ii+1)
#             self.__update__(mid+1, j, k, diff, 2*ii+2)

#     def update(self, i, val):
#         """
#         :type i: int
#         :type val: int
#         :rtype: int
#         """
#         n = len(self.arr)
#         if i < 0 or i > n-1:
#             assert(False)

#         diff = val-self.arr[i]
#         self.arr[i] = val

#         self.__update__(0, n-1, i, diff, 0)

#     def __sum_range__(self, i, j, ii, jj, k):
#         """
#         i and j are boundary index of the node
#         ii and jj are boundary of query
#         k is the position of node in the tree
#         """
#         # if node range within query range,
#         # return value of node
#         if ii <= i and  jj >= j:
#             return self.st[k]

#         # node range is outside of query range
#         if j < ii or i > jj:
#             return 0

#         # mid = self.get_mid(i, j)
#         mid = i+(j-i)/2
#         return self.__sum_range__(i, mid, ii, jj, 2*k+1) + \
#         self.__sum_range__(mid+1, j, ii, jj, 2*k+2)

#     def sumRange(self, ii, jj):
#         """
#         sum of elements nums[i..j], inclusive.
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         n = len(self.arr)
#         if ii < 0 or jj > n-1 or ii > jj:
#             assert(False)

#         return self.__sum_range__(0, n-1, ii, jj, 0)


# if __name__=="__main__":
#     # ls = [1, 2, 3, 4, 5]
#     ls = [1,3,5]
#     # ,sumRange(0,2),update(1,2),sumRange(0,2)
#     ans = [15, 6, 9, 3, 3, 4, 5, 1, 2, 0, 0, 0, 0, 0, 0]

#     # ls = [1,2,3,4,5]
#     N = NumArray(ls)

#     print N.arr
#     print N.st

#     # N.update(0, 5)

#     # print N.arr
#     # print N.st

#     # print N.sumRange(0, 4)
#     # print N.sumRange(1, 1)
#     # print N.sumRange(1, 3)
#     # print N.sumRange(0, 0)
#     # print N.sumRange(4, 4)
#     # print N.update(1, 2)
#     # print N.sumRange(4, 4)
#     print [n for n in N.st]
#     # print N.sumRange(0, 2)
#     N.update(1,2)
#     # print N.sumRange(0,2)
#     print [n for n in N.st]

# Solution 3: from leetcode solution #3
import math
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.n = len(nums)
        n = self.n

        if n <= 0:
            self.st = []
            self.arr = []
            return

        self.st = [0 for x in range(2*n)]
        self.arr = [x for x in nums]
        self.build_segment_tree(nums)

    def get_mid(self, i, j):
        return i+(j-i)/2

    def build_segment_tree(self, nums):
        n = len(nums)
        # insert leaves
        for i, j in [(x, x+n) for x in range(n)]:
            self.st[j] = nums[i]
        # insert inner nodes bottom up
        for i in range(1, n)[::-1]:
            self.st[i] = self.st[2*i] + self.st[2*i+1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        n = self.n
        i += n
        self.st[i] = val

        # update parents
        while i > 0:
            left = i
            right = i
            if i%2 == 0:
                right = i+1
            else:
                left = i-1
            self.st[i/2] = self.st[left] + self.st[right]
            i /= 2

    def sumRange(self, left, right):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        left += self.n
        right += self.n

        sum_ = 0
        while left <= right:
            if left%2 == 1:
                sum_ += self.st[left]
                left += 1
            if right%2 == 0:
                sum_ += self.st[right]
                right -= 1
            left /= 2
            right /= 2
        return sum_

if __name__=="__main__":
    # ls = [1, 2, 3, 4, 5]
    # ls = [1,3,5]

    # ,sumRange(0,2),update(1,2),sumRange(0,2)
    ans = [15, 6, 9, 3, 3, 4, 5, 1, 2, 0, 0, 0, 0, 0, 0]

    ls = [2, 4, 5, 7, 8, 9]
    ans = [0, 35,29,6,12,17,2,4,5,7,8,9]

    # ls = [1,2,3,4,5]
    N = NumArray(ls)

    # print N.arr
    # print N.st

    # N.update(0, 5)

    # print N.arr
    # print N.st

    # print N.sumRange(0, 4)
    # print N.sumRange(1, 1)
    # print N.sumRange(1, 3)
    # print N.sumRange(0, 0)
    # print N.sumRange(4, 4)
    # print N.update(1, 2)
    # print N.sumRange(4, 4)
    # print [n for n in N.st]
    # print N.sumRange(0, 2)
    # N.update(1,2)
    # print N.sumRange(0,2)
    print ls
    print [n for n in N.st]
    print (0, 0), N.sumRange(0, 0)
    print (0, 1), N.sumRange(0, 1)
    print (0, 2), N.sumRange(0, 2)
    print (0, 4), N.sumRange(0, 4)
    print (2, 4), N.sumRange(2, 4)