class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        new = [gas[i] - cost[i] for i in range(len(gas))]
        
        prefix = [0]
        
        for num in new:
            prefix.append(prefix[-1] + num)
            
        prefix[0] = prefix[-1]
        prefix.pop()
        
        Min = float('inf')
        res = -1
        
        for i,  num in enumerate(prefix):
            if num < Min:
                res = i
                Min = num
                
        return res if prefix[0] >= 0 else -1