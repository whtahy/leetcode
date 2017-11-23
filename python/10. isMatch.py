class Solution:
    def isMatch(self, s, p):
        re_haha = re.compile('^' + p + '$')
        
        # credit to @liangsun for line 7
        # https://discuss.leetcode.com/post/60672
        return re_haha.search(s) is not None
