# credit to @wuyi365:
# https://discuss.leetcode.com/post/42582
class Solution:
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()','').replace('{}','').replace('[]','')
        return s == ''
