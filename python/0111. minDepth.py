# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bfs
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        level = 1
        dq = deque([root])
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                if node.left is None and node.right is None:
                    return level
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            level += 1

# dfs
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return 1 + Solution.minDepth(self, root.right)
        elif root.right is None:
            return 1 + Solution.minDepth(self, root.left)
        else:
            return 1 + min(Solution.minDepth(self, root.left), Solution.minDepth(self, root.right))
