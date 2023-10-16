class Solution:
    def countOrders(self, n: int) -> int:
        curr = 1
        
        for i in range(2, n+1):
            curr = (i * curr * (2 * i - 1)) % (10 ** 9 + 7)
            
        return curr
            
        
        
        