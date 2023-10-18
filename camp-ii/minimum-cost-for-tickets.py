class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @cache
        def dp(idx):
            if idx >= len(days):
                return 0
            
            res = costs[0] + dp(idx + 1)
            curr = idx
            
            while curr < len(days) and days[curr] < days[idx] + 7:
                curr += 1
                
            res = min(res, costs[1] + dp(curr))
            
            while curr < len(days) and days[curr] < days[idx] + 30:
                curr += 1
        
            res = min(res, costs[2] + dp(curr))
            
            return res
        
        return dp(0)