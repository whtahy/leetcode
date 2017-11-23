class Solution:
    def addTwoNumbers(self, l1, l2):
        def collect(ll):
            x,p,i = 0,0,ll
            while i is not None:
                x += i.val * 10 ** p
                p += 1
                i = i.next
            return x

        def to_ll(s):
            if len(s) == 1:
                return ListNode(int(s))
            else:
                out = ListNode(int(s[-1]))
                out.next = to_ll(s[0:-1])
                return out

        a = collect(l1)
        b = collect(l2)

        return to_ll(str(a + b))
