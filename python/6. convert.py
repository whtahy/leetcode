# Credit to @DazzlingHelios:
# https://discuss.leetcode.com/post/36258
class Solution:
    def convert(self, s, n):
        if n <= 1 or len(s) < n:
            return s

        rows, r = [''] * n, 0
        for x in s:
            rows[r] += x
            if r == n-1:
                direction = -1
            elif r == 0:
                direction = 1
            r += direction
        return ''.join(rows)
