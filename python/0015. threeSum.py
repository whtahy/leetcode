class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        while i < len(nums)-2:
            if sum(nums[i:i+3]) > 0:
                break
            j, k = i+1, len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j = bisect.bisect_right(nums, nums[j], lo = j+1)
                    k = bisect.bisect_left(nums, nums[k], hi = k-1)
                elif s < 0:
                    j += 1
                else:
                    k -= 1
            i = bisect.bisect_right(nums, nums[i], lo = i+1)
        return ans
