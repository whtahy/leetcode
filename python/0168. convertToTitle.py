class Solution:
    def convertToTitle(self, n: int) -> str:
        s = []
        while n > 0:
            n -= 1
            s.append(chr(n % 26 + 65))
            n //= 26
        return ''.join(s[::-1])
