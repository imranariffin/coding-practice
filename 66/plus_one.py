"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list."""

class Solution(object):

    def plusOne(self, digits):

        """

        :type digits: List[int]

        :rtype: List[int]

        """

        

        # traverse in reverse

        plus_one = True

        for i in range(len(digits))[::-1]:

            if plus_one:

                digits[i] = (digits[i]+1)%10

            if digits[i] != 0:

                plus_one = False

                

        # overflow

        if plus_one:

            ret = [1]

            for d in digits:

                ret.append(d)

            return ret

                

        # return new list

        return [digit for digit in digits]
