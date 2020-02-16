class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        l = len(nums)

        # forward
        for i in range(l-1):
            if i == l-2:
                return True
            if nums[i] > nums[i+1]:
                break
        else:
            i = 0

        # backward
        for j in range(i, l)[::-1]:
            if j <= 1:
                return True
            if nums[j-1] > nums[j]:
                break

        return j-i == 1 and (nums[i-1] <= nums[j] or nums[i] <= nums[j+1])
