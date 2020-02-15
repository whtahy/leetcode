class Solution:
    def lengthOfLastWord(self, s):
        return len(s.rstrip()[::-1].split(' ', maxsplit=1)[0])

    def lengthOfLastWord_v2(self, s):
        return len(s.rstrip().split(' ')[-1])

    def lengthOfLastWord_v3(self, s):
        s, l = s.rstrip(), 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                break
            else:
                l += 1
        return l
