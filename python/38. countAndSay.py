class Solution:
    def say(self, s):
        hoho = ''
        for n, group in itertools.groupby(s):
            hoho += str(len(list(group))) + n
        return hoho

    def countAndSay(self, n):
        s = '1'
        while n > 1:
            s = self.say(s)
            n -= 1
        return s
