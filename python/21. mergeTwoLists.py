class Solution:
    def to_ls(self, ll):
        ls = []
        node = ll
        while node is not None:
            ls += [node.val]
            node = node.next
        return ls

    def mergeTwoLists(self, ll1, ll2):
        ls1 = self.to_ls(ll1)
        ls2 = self.to_ls(ll2)

        if ls1 is None:
            return ls2
        elif ls2 is None:
            return ls1
        else:
            return sorted(ls1 + ls2)
