class Solution:
    def __init__(self):
        self.parent = None
        self.size = None

    def initialize(self, s1, s2):
        self.parent ={chr(ch): chr(ch) for ch in range(ord('a'), ord('z')+1)}
        self.size = defaultdict(lambda: 1)
        self.min = {chr(ch): chr(ch) for ch in range(ord('a'), ord('z')+1)}


    def find(self, node):
        hold = node

        while node != self.parent[node]:
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

        if rootX == rootY:
            return

        if self.size[rootX] <= self.size[rootX]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
            self.min[rootY] = min(self.min[rootY], self.min[rootX])
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
            self.min[rootX] = min(self.min[rootY], self.min[rootX])

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.initialize(s1, s2)
        for i in range(len(s1)):
            self.union(s1[i], s2[i])

        res = []

        for ch in baseStr:
            res.append(self.min[self.find(ch)])

        return "".join(res)
        