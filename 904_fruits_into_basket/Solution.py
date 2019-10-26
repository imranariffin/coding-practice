class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        ret = -1
        cur_max = -1
        is_valid = False
        i = 0
        j = 0
        tree_map = {}
        last_move = 'j'

        if not tree:
            return 0

        while i <= j:
            # print('i=%s,j=%s,tree[%s]=%s,tree_map=%s,is_valid=%s,ret=%s'%(i, j, j, tree[j], tree_map, is_valid, ret))
            if last_move == 'j':
                cur = tree[j]
                if cur not in tree_map:
                    tree_map[cur] = 1
                else:
                    tree_map[cur] += 1

            is_valid = len(tree_map) <= 2

            if is_valid:
                cur_max = sum(map(lambda k: tree_map[k], tree_map))
                ret = max(ret, cur_max)
                j += 1
                last_move = 'j'
            else:
                left = tree[i]
                if left in tree_map:
                    tree_map[left] -= 1
                    if tree_map[left] == 0:
                        del tree_map[left]
                i += 1
                last_move = 'i'

            if is_valid and j == len(tree):
                break

        return ret

