# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        p, q = headA, headB
        while p is not q:
            p, q = p.next, q.next

            if p is q:
                break
            if not p:
                p = headB
            if not q:
                q = headA

        return p
