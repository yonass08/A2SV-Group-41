class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = [[] for _ in range(n)]
        seen = [False] * n
        res = 0
        
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
            
            
        def dfs(node):
            nonlocal res
            nonlocal k
            
            curr = values[node]
            seen[node] = True
            
            for child in tree[node]:
                if seen[child]:
                    continue
                    
                curr += dfs(child)
                
            if curr % k == 0:
                res += 1
                
            return curr
        
        dfs(0)
        
        return res
                
                    
        