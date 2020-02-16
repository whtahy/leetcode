class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = bisect.bisect_left(nums, target)
        b = bisect.bisect_right(nums, target) - 1
        if a <= b and nums[a] == nums[b]:
            return [a, b]
        else:
            return [-1, -1]
