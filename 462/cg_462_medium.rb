# @param {Integer[]} nums
# @return {Integer}
def min_moves2(nums)
    a = []
    
    for num in nums
        a << num
    end
    
    a = a.sort
    
    m = a[a.length / 2]
    move = 0
    
    for val in a
        move = move + (val - m).abs
    end
    
    return move
end
