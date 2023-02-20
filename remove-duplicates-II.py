# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        fakeHead = ListNode(None, head)
        slow = fakeHead
        fast = slow.next

        
        while fast:
            if fast.next and fast.next.val == fast.val:
                while fast.next and fast.val == fast.next.val:
                    fast = fast.next
                slow.next = fast.next
                
            else:
                slow = slow.next
                
            fast = fast.next
    
        return fakeHead.next
                    
                
        
