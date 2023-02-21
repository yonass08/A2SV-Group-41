# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        i = 0
        stack = []
        res = []
        
        while head:
            res.append(0)
            while stack and head.val > stack[-1][1]:
                item = stack.pop()
                res[item[0]] = head.val
            stack.append((i, head.val))
            i += 1
            head= head.next

        return res
