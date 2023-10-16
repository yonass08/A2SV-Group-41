class Node:
    def __init__(self, key, val, nex):
        self.key = key
        self.val = val
        self.nex = nex

class MyHashMap:

    def __init__(self):
        self.length = 7919
        self.table = [Node(-1, -1, None)] * 10007
        

    def put(self, key: int, value: int) -> None:
        idx = key % self.length
        curr = self.table[idx]
        
        while curr.nex:
            if curr.key == key:
                curr.val = value
                return
            curr = curr.nex
            
        if curr.key == key:
            curr.val = value
            return
            
        curr.nex = Node(key, value, None)
            
                

        

    def get(self, key: int) -> int:
        idx = key % self.length
        curr = self.table[idx]
        
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.nex
            
        return -1
        
        

    def remove(self, key: int) -> None:
        idx = key % self.length
        curr = self.table[idx]
        
        while curr.nex:
            if curr.nex.key == key:
                curr.nex = curr.nex.nex
                return
            curr = curr.nex
            

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)