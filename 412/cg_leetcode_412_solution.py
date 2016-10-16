class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        for i in range(1, n + 1):
            fb = ''
            
            if i % 3 == 0:
                fb += 'Fizz'
                
            if i % 5 == 0:
                fb += 'Buzz'
                
            if fb:
                res += [fb]
            else:
                res += [str(i)]
                
        return res
