class Solution:
    def collect(self, ll):
        x,p,i = 0,0,ll
        while i is not None:
            x += i.val * 10 ** p
            p += 1
            i = i.next
        return x

    def to_ll(self, s):
        if len(s) == 1:
            return ListNode(int(s))
        else:
            out = ListNode(int(s[-1]))
            out.next = self.to_ll(s[0:-1])
        return out

    def addTwoNumbers(self, l1, l2):
        a = self.collect(l1)
        b = self.collect(l2)
        return self.to_ll(str(a + b))
