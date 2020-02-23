# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
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

# iterative
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        m = len(nums) - 1
        i = m // 2
        root = TreeNode(nums[i])

        parents = collections.deque([root])
        children = collections.deque([(0, i-1), (i+1, m)])

        while parents:
            p = parents.popleft()

            # left
            a, b = children.popleft()
            i = (a + b) // 2
            children.append((a, i-1))
            children.append((i+1, b))

            if a <= b:
                p.left = TreeNode(nums[i])
                parents.append(p.left)

            # right
            a, b = children.popleft()
            i = (a + b) // 2
            children.append((a, i-1))
            children.append((i+1, b))

            if a <= b:
                p.right = TreeNode(nums[i])
                parents.append(p.right)

        return root
