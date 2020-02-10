class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)

        nums.sort()

        l = len(nums)
        ans = None
        best = math.inf

        for i, x in enumerate(nums[:l-2]):
            k, j = i+1, l-1
            while k < j:
                total = x + nums[k] + nums[j]
                if total == target:
                    return target
                delta = abs(target - total)
                if delta < best:
                    best = delta
                    ans = total
                if total < target:
                    k += 1
                else:
                    j -= 1
        return ans
