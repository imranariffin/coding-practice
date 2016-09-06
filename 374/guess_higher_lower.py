# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        mid = i+(j-i)/2
        res = guess(mid)

        while True:        	
        	if res == 0:
        		return mid
        	elif res == -1:
        		j = mid-1
        	else:
        		i = mid+1

        	if i == j:
        		return i if guess(i) == 0 else 0

        	mid = i+(j-i)/2
        	res = guess(mid)