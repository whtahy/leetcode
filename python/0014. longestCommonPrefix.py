# vertical scan
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        i = 0
        for x in zip(*strs):
            if not all(x[0] == y for y in x[1:]):
                break
            else:
                i += 1

        return strs[0][:i]

# sort: credit to https://leetcode.com/cassandra9/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()

        i = 0
        for x, y in zip(strs[0], strs[-1]):
            if x != y:
                break
            else:
                i += 1

        return strs[0][:i]
