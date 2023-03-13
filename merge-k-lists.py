# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None

        def merge(list1, list2):
            fakeHead = ListNode(0, None)
            current = fakeHead

            while list1 and list2:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next

            if list1:
                current.next = list1
            else:
                current.next = list2

            return fakeHead.next

        k = len(lists)
        while k > 1:
            for i in range(0, k, 2):
                lists[i//2] = merge(lists[i], lists[i+1] if i+1 < k else None)
            k = (k + 1) // 2
        
        return lists[0]


