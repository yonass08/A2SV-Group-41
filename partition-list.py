# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode(0, None)
        greater = ListNode(0, None)

        less_start = less
        greater_start = greater

        while head:
            if head.val < x:
                less.next = head
                head = head.next
                less = less.next
                less.next = None
            else:
                greater.next = head
                head = head.next
                greater = greater.next
                greater.next = None

        less.next = greater_start.next
        return less_start.next

        

        
