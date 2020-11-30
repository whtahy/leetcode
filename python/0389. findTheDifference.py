# dict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for ch in s:
            d[ch] += 1
        for ch in t:
            d[ch] -= 1
            if d[ch] < 0:
                return ch

# Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        t = Counter(t)
        return next(iter(t - s))

# sort
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for a, b in zip(s, t):
            if a != b:
                return b
        return t[-1]
