class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) < 1:
            return 0

        for i in range(0, len(haystack)):
            if (i + len(needle)) <= len(haystack) and haystack[i:i + len(needle)] == needle:
                return i
        return -1
