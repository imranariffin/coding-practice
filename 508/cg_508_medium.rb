# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer[]}
def find_frequent_tree_sum(root)
    st_sums = Hash.new(0)
    subtree_sum(root, st_sums)
    max_count = st_sums.values.max
    st_sums.select { |k, v| v == max_count }.keys
end

def subtree_sum(node, result)
    return 0 if node.nil?
    st_sum = node.val + subtree_sum(node.left, result) + subtree_sum(node.right, result)
    result[st_sum] += 1
    st_sum
end
