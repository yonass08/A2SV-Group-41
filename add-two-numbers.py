# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        res = curr = ListNode(0, None)

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            temp = val1 + val2 + carry
            curr.next = ListNode(temp % 10, None)
            carry = temp // 10

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return res.next

