class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            s = str(x)
            l = len(s)
            pivot = l // 2
            return s[0: pivot] == s[pivot + l % 2: ][::-1]
