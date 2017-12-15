class Solution:
    def plusOne(self, ls):
        x = int(''.join([str(x) for x in ls]))
        return [int(x) for x in str(x + 1)]
