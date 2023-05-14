class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        queue = deque()
        targets = set()
        seen = [False] * len(routes)

        routeIdx = defaultdict(list)
        for idx, route in enumerate(routes):
            for stop in route:
                routeIdx[stop].append(idx)
                if stop == source:
                    queue.append(idx)
                    seen[idx] = True
                if stop == target:
                    targets.add(idx)

        graph = [[] for _ in range(len(routes))]

        for idx, route in enumerate(routes):
            for stop in route:
                graph[idx].extend(routeIdx[stop])

        count = 1
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr in targets:
                    return count

                for child in graph[curr]:
                    if not seen[child]:
                        queue.append(child)
                        seen[child] = True

            count += 1

        return -1


        

        