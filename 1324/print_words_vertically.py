class Solution:
    def printVertically(self, s: str) -> List[str]:
        d = {}
        h = 0
        for word in s.split(' '):
            h = max(h, len(word))

        for i in range(h):
            d[i] = []

        for word in s.split(' '):
            for i, c in enumerate(word):
                d[i].append(c)
            for i in range(len(word), h):
                d[i].append(' ')

        ret = []
        for i in d:
            ret.append(''.join(d[i]).rstrip())
        return ret
