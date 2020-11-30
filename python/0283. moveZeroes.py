class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        z = 0
        for i in range(1, len(nums)):
            if nums[i] != 0 and nums[z] == 0:
                nums[i], nums[z] = nums[z], nums[i]
            if nums[z] != 0:
                z += 1
