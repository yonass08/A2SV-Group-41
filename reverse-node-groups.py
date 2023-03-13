# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
            
        curr = head
        count = 1

        while curr.next and count < k:
            curr = curr.next
            count += 1

        if count < k:
            return head

        prev = self.reverseKGroup(curr.next, k)
        curr.next = None
        curr = head

        # reverse it 
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

        
        
