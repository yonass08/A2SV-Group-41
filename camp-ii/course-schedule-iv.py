class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre = [set() for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)


        while queue:
            curr = queue.popleft()

            for child in graph[curr]:
                indegree[child] -= 1
                pre[child].add(curr)
                pre[child].update(pre[curr])

                if indegree[child] > 0:
                    continue
                queue.append(child)

        res = []
        for u, v in queries:
            res.append(u in pre[v])


        return res