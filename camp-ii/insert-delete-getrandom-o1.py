class RandomizedSet:

    def __init__(self):
        self.index = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        
        self.list.append(val)
        self.index[val] = len(self.list) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        
        idx = self.index[val]
        self.list[idx] = self.list[-1]
        self.index[self.list[-1]] = idx
        self.list.pop()
        del self.index[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()