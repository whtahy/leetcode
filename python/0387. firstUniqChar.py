class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, x in enumerate(s):
            if counts[x] == 1:
                return i
        return -1
