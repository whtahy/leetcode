# sqrt
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(sqrt(num)) ** 2 == num

# Babylonian method, aka Heron's method, Newton-Raphson
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        x = num/2
        while x ** 2 - num > 1:
            x = (x + num / x) / 2
        return round(x) ** 2 == num

