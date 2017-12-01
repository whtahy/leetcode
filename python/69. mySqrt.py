# credit to @StefanPochmann and Wikipedia
# https://discuss.leetcode.com/post/26217
class Solution:
    def mySqrt(self, x):
        rt = x
        while rt ** 2 > x:
            rt = (rt + x // rt) // 2
        return rt
