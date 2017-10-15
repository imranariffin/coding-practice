class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ret = []
        for h in range(12):
            for m in range(60):
                bit = bin(((h & 15) << 6) | (m & 127))
                if bit.count("1") == num:
                    ret.append("%d:%02d" % (h, m))
        return ret
