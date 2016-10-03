"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. 
For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers 
given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k <= 100, 0 < n <= 106, 0 < primes[i] < 1000.
"""
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        ls_superugly = [1]
        n = 2
    	while len(ls_superugly) < n:
    		if self.is_ugly(n, primes):
    			ls_superugly.append(n)

    		n += 1

    	print ls_superugly
    	ret = ls_superugly.pop()    	
    	print ret
    	return ret

    def is_ugly(self, n, primes):

    	if n <= 0:
    		return False

    	while n > 1:
    		is_any_factor = False
    		for prime in primes:
    			if n%prime == 0:
    				n /= prime
    				is_any_factor = True

    		if not is_any_factor:
    			return False

    	return True


if __name__=="__main__":

	ls_primes = [2, 3, 5, 13, 19, 29, 31, 37, 43, 47, 53, 61, 67, 83, 95, 97, 201, 203, 207, 311, 317]
	ls_n = [n for n in range(10000)]
	s = Solution()

	print ls_primes
	for n in ls_n:
		print n, s.is_ugly(n, ls_primes)

# Richard's:
# class Solution:
#     # @param {int} n a positive integer
#     # @param {int[]} primes the given prime list
#     # @return {int} the nth super ugly number
#     def nthSuperUglyNumber(self, n, primes):
#         import heapq
#         length = len(primes)
#         times = [0] * length
#         uglys = [1]
#         minlist = [(primes[i] * uglys[times[i]], i) for i in xrange(len(times))]
#         heapq.heapify(minlist)
        
#         while len(uglys) < n:
#             print minlist, uglys, times
#             (umin, min_times) = heapq.heappop(minlist)
#             print minlist, uglys, times, umin, min_times
            
#             times[min_times] += 1
#             if umin != uglys[-1]:
#                 uglys.append(umin)
#             heapq.heappush(minlist, (primes[min_times] * uglys[times[min_times]], min_times))

#         return uglys[-1] 
              
# print Solution().nthSuperUglyNumber(8, [2,3,5]) == 1