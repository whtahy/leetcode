class Solution:
    def expand(self, s, i):
        left = i // 2 - (i % 2 == 0)
        right = i // 2 + 1
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1

    def get_p(self, s, i, r):
        pivot = i // 2
        return s[pivot - r  + (i % 2 == 1): pivot + r + 1]

    def longestPalindrome(self, s):
        n = 2 * len(s) - 1
        ls = [0] * n

        for i in range(n):
            ls[i] = self.expand(s, i)

        i_max = ls.index(max(ls))
        r = ls[i_max] // 2
        return self.get_p(s, i_max, r)
