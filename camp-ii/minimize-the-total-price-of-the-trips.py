class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = [[] for _ in range(n+1)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
       
        count = Counter()
    
        totalCost = 0

        def dfs(node,parent,end):
            nonlocal count
            nonlocal totalCost
            if node == end:
                return True
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    if dfs(neighbor, node, end):
                        count[neighbor] += 1
                        totalCost += price[neighbor]
                        return True
            return False

       
        for start,end in trips:
            count[start] += 1
            totalCost += price[start]
            dfs(start,None,end)
        
      
        @cache
        def dp(node, parent, canReduce):
            if canReduce:
                res = (price[node]//2)*count[node]
            else:
                res = 0
            red = 0
            for neighbor in graph[node]:
                if neighbor != parent:
               
                    if canReduce:
                        cur = dp(neighbor, node, False)

                    else:
                        cur = max(dp(neighbor, node, False), dp(neighbor, node, True))
                    red += cur
            return res + red
        
    
        reduce = 0
        for i in range(n):
            reduce = max( reduce, dp(i, None, True), dp(i, None, False) )
        
    
        return totalCost - reduce