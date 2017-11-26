# credit to @lucastan:
# https://discuss.leetcode.com/post/5085
class Solution:
    def maxSubArray(self, ls):
        _sum, _max = ls[0], ls[0]
        for x in ls[1:]:
            _sum += x
            _sum = max(x, _sum)
            _max = max(_sum, _max)
        return _max
