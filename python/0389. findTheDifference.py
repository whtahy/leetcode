# 1 Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(s)
        for ch in t:
            if c[ch] == 0:
                return ch
            c[ch] -= 1

# 2 Counters
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        t = Counter(t)
        return next(iter(t - s))

# 2 sorts
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for a, b in zip(s, t):
            if a != b:
                return b
        return t[-1]
