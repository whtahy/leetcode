class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        s = deque(s)
        for ch in t:
            if ch == s[0]:
                s.popleft()
            if len(s) == 0:
                return True
        return False
