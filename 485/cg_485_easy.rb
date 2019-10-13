# @param {Integer[]} nums
# @return {Integer}
def find_max_consecutive_ones(nums)
    max_count = 0
    cur_count = 0
    
    nums.each do |b|
        b == 1 ? cur_count += 1 : cur_count = 0
        
        max_count = cur_count if cur_count > max_count
    end
    
    max_count
end
