class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        x = round(log(n, 3))
        return n == 3 ** x
