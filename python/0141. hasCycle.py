# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        a, b = head, head.next
        while b and b.next and b.next.next:
            if a is b:
                return True
            a = a.next
            b = b.next.next
        return False
