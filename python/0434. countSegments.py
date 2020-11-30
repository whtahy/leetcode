# split
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

# for loop
class Solution:
    def countSegments(self, s: str) -> int:
        n = 0
        is_new = True
        for ch in s:
            if is_new and ch != ' ':
                n += 1
                is_new = False
            elif ch == ' ':
                is_new = True
        return n
