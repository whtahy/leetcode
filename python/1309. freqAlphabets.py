class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s)-1
        t = []
        while i >= 0:
            if s[i] == '#':
                x = s[i-2:i]
                i -= 3
            else:
                x = s[i]
                i -= 1
            t.append(chr(int(x)+96))
        return ''.join(t[::-1])
