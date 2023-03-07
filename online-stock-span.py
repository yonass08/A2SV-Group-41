class StockSpanner:

    def __init__(self):
        self.stocks = []
        self.stack = [-1]
        

    def next(self, price: int) -> int:
        while len(self.stack) > 1 and price > self.stocks[self.stack[-1]]:
            self.stack.pop()

        res = 0

        idx = len(self.stack) - 1 
        while idx > 0 and price == self.stocks[self.stack[idx]]:
            idx -= 1
            
        res = len(self.stocks) - self.stack[idx]
        self.stack.append(len(self.stocks))

        self.stocks.append(price)
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
