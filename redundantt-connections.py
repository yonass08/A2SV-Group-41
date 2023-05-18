class Solution:
    def __init__(self):
        self.parent = None
        self.size = None

    def initialize(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

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

        if self.size[rootX] <= self.size[rootY]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.initialize(len(edges)+1)
        for a, b in edges:
            if self.find(a)  == self.find(b):
                return [a, b]
            self.union(a, b)
        return []
