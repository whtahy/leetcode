# credit to @caikehe:
# https://discuss.leetcode.com/post/24304
class Solution:
    def threeSum(self, ls):
        ls.sort()
        threes = []
        _len, prev = len(ls), None
        for i in range(_len - 2):
            if sum(ls[i: i + 3]) > 0:
                break
            elif ls[i] == prev:
                continue
            prev = ls[i]
            l, r = i + 1, _len - 1
            while l < r:
                _sum = ls[i] + ls[l] + ls[r]
                if _sum < 0:
                    l += 1
                elif _sum > 0:
                    r -= 1
                else:
                    threes += [[ls[i], ls[l], ls[r]]]
                    l = bisect.bisect_right(ls, ls[l])
                    r = bisect.bisect_left(ls, ls[r]) - 1
        return threes
