class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for n in arr:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1

        nums = [(num, count) for num, count in d.items()]
        nums.sort(key=lambda x: -x[1])

        ret = 0
        curr = 0
        half = len(arr) / 2
        for num, count in nums:
            if curr >= half:
                return ret
            curr += count
            ret += 1

        return ret

