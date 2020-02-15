# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 1 and not head.next:
            return None

        tmp = []
        node = head
        while node:
            tmp.append(node)
            node = node.next
        tmp.append(None)
        l = len(tmp) - 1

        if n == l:
            return tmp[1]

        tmp[l-n-1].next = tmp[l-n+1]
        return head
