class Solution:
    def twoSum(self, ls, _sum):
        d = {}
        for i, x in enumerate(ls):
            y = _sum - x
            if y not in d:
                d[x] = i
            else:
                return d[y], i
