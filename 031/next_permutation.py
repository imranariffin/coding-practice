class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        possible = False
        i = nums[0]
        for j in nums[1:]:
            if j > i:
                possible = True
                break
            i = j
        if not possible:
            nums.sort()
            return

        print "nums: ", nums
        # find longest non-increasing suffix
        lni_suffix = self.longest_non_increasing_suff(nums)
        print "lni_suffix: ", lni_suffix
        
        # swap pivot with smallest number in suffix that's bigger than pivot
        pivot = len(nums) - len(lni_suffix) - 1
        self.swap_pivot_suffix(nums, pivot)
        print "nums: ", nums

        # reverse suffix
        reversed_suff = nums[pivot+1:][::-1]
        for i in range(len(reversed_suff)):
            nums[pivot+i+1] = reversed_suff[i]

        print "nums: ", nums


    def longest_non_increasing_suff(self, nums):
        i = len(nums)-1
        pivot = len(nums)-1
        for j in range(len(nums)-1)[::-1]:
            if nums[j] < nums[i]:
                pivot = j
                break
            i = j

        return list(nums[pivot+1:])

    def swap_pivot_suffix(self, nums, pivot):
        num_pivot = nums[pivot]
        i_swap = len(nums)-1
        min_num = nums[i_swap]
        for i in range(pivot+1, len(nums))[::-1]:
            num = nums[i]
            if num > num_pivot:
                min_num = num
                i_swap = i
                break

        temp = nums[i_swap]
        nums[i_swap] = num_pivot
        nums[pivot] = temp

if __name__=="__main__":
    s = Solution()
    s.nextPermutation([0, 1, 2, 5, 3, 3, 0])