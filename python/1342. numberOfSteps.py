# bit shift
class Solution:
    def numberOfSteps (self, num: int) -> int:
        n = 0
        while num:
            n += (num & 1) + 1
            num >>= 1
        return n-1

# naive
class Solution:
    def numberOfSteps (self, num: int) -> int:
        n = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            n += 1
        return n
