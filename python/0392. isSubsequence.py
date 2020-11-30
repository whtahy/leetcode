# 2 pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

# dictionary + binary search
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        d = defaultdict(list)
        for i, ch in enumerate(t):
            d[ch].append(i)

        i = -1
        for ch in s:
            j = bisect_left(d[ch], i)
            if j == len(d[ch]):
                return False
            i = d[ch][j] + 1
        return True
