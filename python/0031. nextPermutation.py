class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        l = len(nums)

        if all(nums[i] >= nums[i+1] for i in range(l-1)):
            nums.reverse()
            return None

        # find pivot
        for i in reversed(range(l-1)):
            if nums[i] < nums[i+1]:
                break

        # find swap
        for j in reversed(range(l)):
            if nums[j] > nums[i]:
                break

        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = reversed(nums[i+1:])

        return None
