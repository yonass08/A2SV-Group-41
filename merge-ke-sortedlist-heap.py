# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None

        dummy = ListNode()
        curr = dummy
        heap = []

        for i, head in enumerate(lists):
            if head:
                heappush(heap, (head.val, i, head))

        while heap:
            curr_min, idx, curr_ptr = heappop(heap)
            temp = curr_ptr.next
            curr_ptr.next = None

            curr.next = curr_ptr
            curr = curr.next

            if temp:
                heappush(heap, (temp.val, idx, temp))
        
        return dummy.next

        
        
        


