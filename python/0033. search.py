class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        a, b = 0, len(nums)-1
        target_left = target >= nums[0]
        target_right = not target_left

        while a <= b:
            i = (a + b) // 2

            if nums[i] == target:
                return i

            # same side
            if (target_left and nums[i] >= nums[0]) \
                    or (target_right and nums[i] < nums[0]):
                if nums[i] < target:
                    a = i + 1
                else:
                    b = i - 1
            # backwards
            else:
                if nums[i] < target:
                    b = i - 1
                else:
                    a = i + 1

        return -1
