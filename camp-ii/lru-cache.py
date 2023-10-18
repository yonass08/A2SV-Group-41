class Node:
    def __init__(self, prev, key, val, nex):
        self.prev = prev
        self.key = key
        self.val = val
        self.next = nex

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(None, -1, -1, None)
        self.tail = self.head
        self.Node = {}
        
        
    def update(self, key: int) -> None:
        node = self.Node[key]
        if node == self.tail:
            return 
        
        node.prev.next = node.next
        node.next.prev = node.prev
        self.tail.next = node
        node.next = None
        node.prev = self.tail
        self.tail = node
        

    def get(self, key: int) -> int:
        if key not in self.Node:
            return -1
    
        self.update(key)
        return self.Node[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.Node:
            self.Node[key].val = value
            self.update(key)
            return
        
        node = Node(self.tail, key, value, None)
        self.tail.next = node
        self.tail = node
        self.Node[key] = node
        self.capacity -= 1
        
        if self.capacity < 0:
            dkey = self.head.next.key
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            del(self.Node[dkey])
            self.capacity += 1
            
            
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)