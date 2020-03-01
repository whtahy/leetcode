# naive
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        if k == 0:
            return
        nums[:k], nums[k:] = nums[-k:], nums[:-k]

# reverse
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i, n = 0, len(nums)
        k %= n

        if n <= 1 or k == 0:
            return

        nums.reverse()

        # rotate left
        for i in range(k//2):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]

        # rotate right
        for i in range((n-k)//2):
            nums[k+i], nums[n-i-1] = nums[n-i-1], nums[k+i]

# juggling
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i, n = 0, len(nums)
        k %= n

        if n <= 1 or k == 0:
            return

        tmp, nums[0] = nums[0], None
        for _ in range(n):
            if i < n-k:
                tmp, nums[i+k] = nums[i+k], tmp
                i = i+k
            else:
                tmp, nums[i-(n-k)] = nums[i-(n-k)], tmp
                i = i-(n-k)
            if tmp is None:
                i += 1
                tmp, nums[i] = nums[i], None
        nums[i] = tmp
