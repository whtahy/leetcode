# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(a, b):
            if a > b:
                return None
            i = (a + b) // 2
            node = TreeNode(nums[i])
            node.left = helper(a, i-1)
            node.right = helper(i+1, b)
            return node

        return helper(0, len(nums)-1) if nums else None
