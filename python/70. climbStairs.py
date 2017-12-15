# credit to @liaison:
# https://discuss.leetcode.com/post/7056
class Solution:
    def climbStairs(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            n1 = 1
            n2 = 2

            for i in range(n - 2):
                count = n1 + n2
                n1 = n2
                n2 = count

            return count
