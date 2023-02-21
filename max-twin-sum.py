# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # create two pointers
        first = head
        # find the first middle of the list
        middle = self.findMiddle(head)
        #reverse the second half
        second = self.reverse(middle)
        middle.next = None

        res = 0
        # add up each pair and find the maximum
        while first and second:
            res = max(res, first.val + second.val)
            first = first.next
            second = second.next

        return res

    def reverse(self, head):
        # reverses the list
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


    def findMiddle(self, head):
        # finds the first middle of the list
        dummy = ListNode(0, head)
        slow = fast = dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow



