# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iterative dfs
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return not root or all(x == y for (x, y) in zip(Solution.dfs(root.left, True), Solution.dfs(root.right, False)))

    def dfs(root, left_to_right):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if left_to_right:
                    stack.append(node.right)
                    stack.append(node.left)
                else:
                    stack.append(node.left)
                    stack.append(node.right)
                yield node.val
            else:
                yield node

# recursive
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return Solution.helper(root.left, root.right)

    def helper(p, q):
        if p and q:
            return p.val == q.val and Solution.helper(p.left, q.right) and Solution.helper(p.right, q.left)

        return p is q
