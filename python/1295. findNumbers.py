class Solution:
    # log
    def helper(x):
        return int(math.log10(x) + 1) % 2 == 0

    # string
    def helper(x):
        return len(str(x)) % 2 == 0

    def findNumbers(self, nums: List[int]) -> int:
        return sum(Solution.helper(x) for x in nums)
