# naive
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]

# Boyer-Moore majority voting
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m, i = None, 0

        for x in nums:
            if i == 0:
                m = x
                i = 1
            elif m == x:
                i += 1
            else:
                i -= 1

        return m
