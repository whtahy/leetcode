class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = sum(int(ch) for ch in str(num))
        return num
