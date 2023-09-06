class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.bigHeap = []

    def addNum(self, num: int) -> None:
        if len(self.smallHeap) == len(self.bigHeap):
            heappush(self.bigHeap, num)
            heappush(self.smallHeap, -heappop(self.bigHeap))
        else:
            heappush(self.smallHeap, -num)
            heappush(self.bigHeap, -heappop(self.smallHeap))
        

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.bigHeap):
            return -self.smallHeap[0]
        if len(self.smallHeap) < len(self.bigHeap):
            return self.bigHeap[0]
        
        return (-self.smallHeap[0] + self.bigHeap[0]) / 2
                
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()