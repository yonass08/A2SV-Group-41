# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        if length == 0 or k % length == 0:
            return head

        k %= length

        curr = head
        for _ in range(length - k - 1):
            curr = curr.next

        next_node = curr.next
        curr.next = None

        curr = next_node
        while curr.next:
            curr = curr.next

        curr.next = head
        return next_node

         
