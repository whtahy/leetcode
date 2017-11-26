class Solution:
    def removeDuplicates(self, nums):
        x = sorted(set(nums))
        for i in range(len(x)):
            nums[i] = x[i]
        return len(x)
