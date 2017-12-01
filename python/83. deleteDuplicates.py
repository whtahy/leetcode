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

    def deleteDuplicates(self, head):
        ls = sorted(set(self.to_ls(head)))
        return self.to_ll(ls)
