class MyCircularDeque:

    def __init__(self, k: int):
        self.curr = 0
        self.max = k
        self.list = [0] * k
        self.front = 0
        self.last = k-1
        
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.list[self.front] = value
        self.front = (self.front + 1) % self.max
        self.curr += 1

        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.list[self.last] = value
        self.last = (self.last - 1) % self.max
        self.curr += 1

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front - 1) % self.max
        self.curr -= 1

        return True


    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.last = (self.last + 1) % self.max
        self.curr -= 1

        return True
        

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.list[(self.front-1) % self.max]
        

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.list[(self.last+1) % self.max]
        

    def isEmpty(self) -> bool:
        return self.curr == 0
        

    def isFull(self) -> bool:
        return self.curr == self.max
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
