class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = round(n * (n+1) / 2)
        return int(total) - sum(nums)
