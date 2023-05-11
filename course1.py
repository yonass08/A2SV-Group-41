class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        queue = deque()
        incoming = [0] * numCourses
        possibleCourses = 0

        for post, pre in prerequisites:
            graph[pre].append(post)
            incoming[post] += 1

        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)
                
        while queue:
            curr = queue.popleft()
            possibleCourses += 1

            for post in graph[curr]:
                incoming[post] -= 1
                if incoming[post] == 0:
                    queue.append(post)

        return possibleCourses == numCourses

