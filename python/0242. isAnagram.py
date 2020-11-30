# 2 Counters
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = Counter(s)
        t = Counter(t)
        return len(s - t) == 0

# 1 Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c = Counter(s)
        for ch in t:
            if c[ch] == 0:
                return False
            c[ch] -= 1
        return True
