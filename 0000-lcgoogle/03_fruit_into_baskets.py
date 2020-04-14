from collections import Counter


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        i = 0
        j = 0
        maxcount = 0
        N = len(tree)
        basket = Counter()

        while j < N:
            if len(basket) <= 2:
                fruit = tree[j]
                basket[fruit] += 1
                if len(basket) <= 2:
                    maxcount = max(maxcount, sum(basket.values()))
                j += 1
            else:
                fruit = tree[i]
                basket[fruit] -= 1
                if basket[fruit] == 0:
                    del basket[fruit]
                i += 1

        return maxcount

