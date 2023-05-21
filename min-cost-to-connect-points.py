class Solution:
    def initialize(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        hold = x
        while self.parent[x] != x:
            x = self.parent[x]

        while self.parent[hold] != x:
            temp = self.parent[hold]
            self.parent[hold] = x
            hold = temp

        return x

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return

        if self.size[xroot] > self.size[yroot]:
            self.parent[yroot] = xroot
            self.size[xroot] += self.size[yroot]
        else:
            self.parent[xroot] = yroot
            self.size[yroot] += self.size[xroot]

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.initialize(len(points))
        edges = []

        manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges.append((manhattan(points[i], points[j]), i , j))

        edges.sort()
        res = 0

        for cost, i, j in edges:
            if self.find(i) != self.find(j):
                self.union(i, j)
                res += cost

        return res