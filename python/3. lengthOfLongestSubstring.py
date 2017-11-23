class Solution:
    def lengthOfLongestSubstring(self, s):
        d, maxlen, start = {}, 0, 0
        for i,l in enumerate(s):
            if l not in d or d[l] < start:
                d[l] = i
            else:
                maxlen = max(maxlen, i - start)
                if s[i] == s[i-1]:
                    start = i
                else:
                    start = d[l]+1
                d[l] = i
        return max(maxlen, len(s) - start)
