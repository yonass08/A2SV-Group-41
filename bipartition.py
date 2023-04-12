class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colors = [0] * (n+1)
        adjList = [[] for _ in range(n+1)]

        for start, end in dislikes:
            adjList[start].append(end)
            adjList[end].append(start)

        def dfs(person, color):
            colors[person] = color
            nextCol = color % 2 + 1

            for dislike in adjList[person]:
                if colors[dislike] == nextCol:
                    continue
                if colors[dislike] == color:
                    return False
                if not dfs(dislike, nextCol):
                    return False

            return True

        for person in range(1, n+1):
            if colors[person] == 0:
                if not dfs(person, 1):
                    return False

        return True
