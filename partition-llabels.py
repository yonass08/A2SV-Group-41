class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        res = []
        slow = 0
        found = defaultdict(int)
        remaining = 0
        
        for fast in range(len(s)):
            if s[fast] not in found:
                remaining += 1
                
            found[s[fast]] += 1
            if found[s[fast]] == counter[s[fast]]:
                remaining -= 1
                
            if remaining == 0:
                res.append(fast - slow + 1)
                slow = fast + 1
                
        return res
            
        
