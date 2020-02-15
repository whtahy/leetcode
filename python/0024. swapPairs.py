# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = head.next
        while node.next and node.next.next:
            node.next = Solution.swap(node.next)
            node = node.next.next
        return Solution.swap(head)

    def swap(node):
        node, node.next, node.next.next = node.next, node, node.next.next
        return node
