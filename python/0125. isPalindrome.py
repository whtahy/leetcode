# slice
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = [ch.lower() for ch in s if ch.isalnum()]
        l = len(t)
        return t[:l//2] == t[l//2+l%2:][::-1]

# two pointer
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

