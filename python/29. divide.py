class Solution:
    def divide(self, a, b):
        x = abs(a)
        y = abs(b)
        if x < y or x == 0:
            return 0
        else:
            i = int(math.exp(math.log(x) - math.log(y)))
        if (a < 0) != (b < 0):
            i = 0 - i
        return min(i, 2147483647)
