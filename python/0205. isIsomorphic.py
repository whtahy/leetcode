# pigeonhole
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

# two dict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dx, dy = {}, {}
        for x, y in zip(s, t):
            if (x in dx and dx[x] != y) or (y in dy and dy[y] != x):
                return False
            dx[x], dy[y] = y, x
        return True
