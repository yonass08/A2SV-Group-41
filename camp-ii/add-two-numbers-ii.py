# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):
            curr = head
            prev = None 
            
            while curr:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
            
            return prev
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        
        head = ListNode()
        curr = head
        carry = 0
        
        while l1 or l2 or carry:
            curr.next = ListNode()
            curr = curr.next
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            curr.val = val1 + val2 + carry
            carry = curr.val // 10
            curr.val %= 10
            
            
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            
        return reverse(head.next)
            
                
                
        