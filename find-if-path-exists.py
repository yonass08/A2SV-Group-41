class Solution:
    def __init__(self):
        self.parent = None
        self.rank = None

    def initialize(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, node):
        hold = node

        while self.parent[node] != node:
            node = self.parent[node]

        res = node

        while self.parent[hold] != res:
            temp = self.parent[hold]
            self.parent[hold] = res
            hold = temp

        return res

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
 
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.initialize(n)
        for u, v in edges:
            self.union(u, v)

        return self.find(source) == self.find(destination)
