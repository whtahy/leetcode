# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# iterative dfs
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        stack = [(root, 0)]
        while stack:
            node, path_sum = stack.pop()
            path_sum += node.val
            if node.left is None and node.right is None and path_sum == sum:
                return True
            if node.left:
                stack.append((node.left, path_sum))
            if node.right:
                stack.append((node.right, + path_sum))

# recursive dfs
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        elif root.left is None and root.right is None and root.val == sum:
            return True

        return Solution.hasPathSum(self, root.left, sum-root.val) \
            or Solution.hasPathSum(self, root.right, sum-root.val)
