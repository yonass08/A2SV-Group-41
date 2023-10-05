class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n+1)]
        distance =[0] * (n+1)
        distance[start_node] = 1
        
        idx = 0
        for u, v in edges:
            graph[u].append((v, succProb[idx]))
            graph[v].append((u, succProb[idx]))
            idx += 1

        heap = [(-1, start_node)]
        seen = set()

        while heap:
            dist, curr = heappop(heap)
            dist *= -1
            if curr in seen:
                continue

            if curr == end_node:
                return dist

            seen.add(curr)

            for child, prob in graph[curr]:
                new_dist = dist * prob
                if new_dist > distance[child]:
                    heappush(heap, (-new_dist, child))

        return 0

            
        
        
        