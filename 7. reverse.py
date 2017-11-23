class Solution:
    def reverse(self, x):
        min_x = -(2 ** 31)
        max_x = 2 ** 31 - 1
        s = str(x)
        if s.startswith('-'):
            s = '-' + s[:0:-1]
        else:
            s = s[::-1]

        r = int(s)
        if min_x <= r <= max_x:
            return r
        else:
            return 0
