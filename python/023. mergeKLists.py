class Solution:
    def to_ls(self, ll):
        ls = []
        node = ll
        while node is not None:
            ls += [node.val]
            node = node.next
        return ls

    def to_ll(self, ls):
        if len(ls) == 0:
            return []
        else:
            # credit to @Hermann0:
            # https://leetcode.com/problems/merge-k-sorted-lists/solution/
            head = pointer = ListNode(None)
            for x in ls:
                pointer.next = ListNode(x)
                pointer = pointer.next
            return head.next

    def mergeKLists(self, lists):
        biglist = []
        for node in lists:
            ls = self.to_ls(node)
            if ls is not None:
                biglist += ls
        biglist.sort()
        return self.to_ll(biglist)
