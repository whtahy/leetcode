class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        history = set()
        for i, x in enumerate(nums):
            if x in history:
                return True
            history.add(x)
            if len(history) > k:
                history.remove(nums[i-k])
        return False
