class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        # sort in descending order
        ls_score = [score for score in citations]
        ls_score.sort(reverse=True)
        print ls_score

        # find i >= A[i]
        if len(ls_score) == 0:
        	return 0
        if len(ls_score) == 1:
        	return 1 if ls_score[0] > 0 else 0
        h = 0
        for i in range(len(ls_score)):
        	# if ls_score[i] >= i and i >= ls_score[i+1]:
        	# 	h = i
        	# 	break
        	if ls_score[i] > h:
        		h += 1
        	else:
        		break
        return h

if __name__=="__main__":

	s = Solution()
	print s.hIndex([3, 0, 6, 1, 5])
	print s.hIndex([1000, 1])