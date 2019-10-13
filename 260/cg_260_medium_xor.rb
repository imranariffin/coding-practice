# @param {Integer[]} nums
# @return {Integer[]}
def single_number(nums)
    signature = 0
    
    nums.each { |x| signature ^= x }
    
    bit_m = 1
    
    bit_m = bit_m << 1 while (signature & bit_m) == 0
    
    arr_p = nums.select { |x| (x & bit_m) != 0 }
    arr_n = nums.select { |x| (x & bit_m) == 0 }
    
    num_1 = 0
    num_2 = 0
    
    arr_p.each { |x| num_1 ^= x }
    arr_n.each { |x| num_2 ^= x }
    
    [num_1, num_2]
end
