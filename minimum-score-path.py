class Solution:
    def __init__(self):
        self.parent = None
        self.size = None
        self.ans = None

    def initialize(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.ans = [float('inf')] * n

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


    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.initialize(n+1)

        for a, b, w in roads:
            nmin = min(w, self.ans[self.find(a)], self.ans[self.find(b)])
            self.union(a, b)
            self.ans[self.find(a)] = nmin

        return self.ans[self.find(1)]

        