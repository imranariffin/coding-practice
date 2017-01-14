# @param {Integer[]} nums
# @return {Integer[]}
def single_number(nums)
    h = Hash.new(0)
    
    nums.each { |num| h[num] += 1 }
    
    res = []
    
    h.each { |k, v| res << k if v == 1 }
    
    res
end
