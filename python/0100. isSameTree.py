# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iterative dfs
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        for (x, y) in zip(Solution.dfs(p), Solution.dfs(q)):
            if x != y:
                return False
        return True

    def dfs(root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)
                yield node.val
            else:
                yield node

# recursive
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return p is q
