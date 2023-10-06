class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        cost_list = defaultdict(int)
        adj_list = defaultdict(set)
        for u, v, w in times:
            cost_list[(u-1,v-1)] = w
            adj_list[u-1].add(v-1)
        time = [float('inf')]*n
        time[k-1] = 0
        priority_queue = [(0, k-1)]
        vis = set()
        while priority_queue:
            cost, node = heapq.heappop(priority_queue)
            if node in vis:
                continue
            vis.add(node)

            for next in adj_list[node]:
                new_cost = cost + cost_list[(node, next)]
                if new_cost < time[next]:
                    time[next] = new_cost
                    heapq.heappush(priority_queue, (new_cost, next))
        ans = max(time)
        if ans == float('inf'):
            return -1
        return ans