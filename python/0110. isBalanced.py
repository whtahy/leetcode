# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return Solution.height(root) != -1

    def height(root: TreeNode) -> int:
        if root is None:
            return 0

        h_left = Solution.height(root.left)
        if h_left == -1:
            return -1

        h_right = Solution.height(root.right)
        if h_right == -1:
            return -1

        if abs(h_left - h_right) > 1:
            return -1

        return max(h_left, h_right) + 1
