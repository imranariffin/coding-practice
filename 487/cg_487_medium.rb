# @param {Integer[]} nums
# @return {Integer}
def find_max_consecutive_ones(nums)
    max_count = 0
    cur_count = 0
    counts = []
    
    for i in 0 ... nums.length
        b = nums[i]
        
        if b == 1
            cur_count += 1
        end
        
        if b != 1 || i == nums.length - 1
            counts << cur_count
            cur_count = 0
        end
        
        max_count = cur_count if cur_count > max_count
    end
    
    if counts.length < 2
        return max_count + 1 <= nums.length ? max_count + 1 : max_count
    end
    
    for i in 1 ... counts.length
        max_count = counts[i] + counts[i - 1] + 1 if counts[i] + counts[i - 1] + 1 > max_count
    end
    
    max_count
end
