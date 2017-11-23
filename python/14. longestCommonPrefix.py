# credit to @cassandra9
# https://discuss.leetcode.com/post/29598
class Solution:
    def longestCommonPrefix(self, ls):
        if len(ls) == 0:
            return ''

        q = sorted(ls)
        x,y = q[0], q[-1]

        i = 0
        for a,b in zip(x,y):
            if a == b:
                i += 1
            else:
                break

        return x[0:i]
