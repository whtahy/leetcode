class Solution:
    def titleToNumber(self, s: str) -> int:
        n = 0
        for i, ch in enumerate(s[::-1]):
            n += (ord(ch)-64) * 26 ** i
        return n
