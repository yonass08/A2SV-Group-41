class MyLinkedList:

    def __init__(self):
        self.fake_head = ListNode(0, None)
        self.size = 0

    def get(self, index):
        if index >= self.size:
            return -1

        curr_node = self.fake_head
        for _ in range(index+1):
            curr_node = curr_node.next

        return curr_node.val

    def addAtHead(self, val):
        new_node = ListNode(val, self.fake_head.next)
        self.fake_head.next = new_node
        self.size += 1

    def addAtTail(self, val):
        curr_node = self.fake_head

        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = ListNode(val, None)
        self.size += 1

    def addAtIndex(self, index, val):
        if index > self.size:
            return

        curr_node = self.fake_head
        for _ in range(index):
            curr_node = curr_node.next

        new_node = ListNode(val, curr_node.next)
        curr_node.next = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        if index >= self.size:
            return 

        curr_node = self.fake_head
        for _ in range(index):
            curr_node = curr_node.next

        curr_node.next = curr_node.next.next
        self.size -= 1
       

        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
