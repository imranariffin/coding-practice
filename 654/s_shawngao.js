/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
const constructMaximumBinaryTree = (nums) => {
  const start = 0
  const end = nums.length - 1
  return build(nums, start, end)
}

// Return the max node that should be somewhere in between [start, end].
const build = (nums, start, end) => {
  // We should stop and the parent node will have a null for one its child node (maybe both if
  // the other child node also happens to be null).
  if (start > end) return null

  // Find the index of the maximum value to be set as the parent node.
  let maxIndex = start
  for (let i = start + 1; i <= end; i++) {
    if (nums[i] > nums[maxIndex]) {
      maxIndex = i
    }
  }

  const root = new TreeNode(nums[maxIndex])

  // Recursively do the same thing for the left and right children. The left child should get the
  // left portion of the array and the right child should get the right.
  root.left = build(nums, start, maxIndex - 1)
  root.right = build(nums, maxIndex + 1, end)

  return root
}
