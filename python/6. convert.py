# Credit to @DazzlingHelios:
# https://discuss.leetcode.com/topic/34573/python-o-n-solution-in-96ms-99-43
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
