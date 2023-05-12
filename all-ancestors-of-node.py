class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        resSet = [set()  for _ in range(n)]
        incoming = [0] * n

        graph = [[] for _ in range(n)]

        for frm, to in edges:
            graph[frm].append(to)
            incoming[to] += 1

        queue = deque()
        for i in range(n):
            if incoming[i] == 0:
                queue.append(i)

        while queue:
            curr = queue.popleft()

            for child in graph[curr]:
                resSet[child].add(curr)
                resSet[child].update(resSet[curr])
                incoming[child] -= 1

                if incoming[child] == 0:
                    queue.append(child)

        return [sorted(res) for res in resSet]
