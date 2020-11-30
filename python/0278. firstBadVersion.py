# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n
        while left < right:
            i = (left + right) // 2
            if isBadVersion(i):
                right = i
            else:
                left = i + 1
        return left
