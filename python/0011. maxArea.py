class Solution:
    def maxArea(self, ls):
        n = len(ls) - 1
        v, left, right = [], 0, n
        while 0 <= left < right <= n:
            h = min(ls[left], ls[right])
            v += [h * (right - left)]
            while ls[left] <= h and left < right:
                left += 1
            while ls[right] <= h and left < right:
                right -= 1
        return max(v)
