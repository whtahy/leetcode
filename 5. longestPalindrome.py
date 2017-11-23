class Solution:
    def longestPalindrome(self, s):
        def expand(i):
            left = i // 2 - (i % 2 == 0)
            right = i // 2 + 1
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return right - left - 1

        def get_p(i):
            r = l_max // 2
            pivot = i // 2
            return s[pivot - r  + (i % 2 == 1): pivot + r + 1]

        n = 2 * len(s) - 1
        ls = [0] * n

        for i in range(n):
            ls[i] = expand(i)

        i_max = ls.index(max(ls))
        l_max = ls[i_max]
        return get_p(i_max)
