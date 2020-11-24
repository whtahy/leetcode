class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        x = round(log(n, 2))
        return n == 2 ** x
