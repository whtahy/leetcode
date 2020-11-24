class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        x = round(log(n, 4))
        return n == 4 ** x
