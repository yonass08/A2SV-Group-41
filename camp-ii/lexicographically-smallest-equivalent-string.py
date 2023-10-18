class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        parent = {ch: ch for ch in alphabet}
        size = {ch: 1 for ch in alphabet}
        smallest = {ch: ch for ch in alphabet}
        
        def find(x):
            root = x
            while parent[root] != root:
                root = parent[root]
            
            while parent[x] != root:
                par = parent[x]
                parent[x] = root
                x = par
                
            return root
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return
            
            if size[x] < size[y]:
                parent[rootx] = rooty
                size[rooty] += size[rootx]
                smallest[rooty] = min(smallest[rootx], smallest[rooty])
            else:
                parent[rooty] = rootx
                size[rootx] += size[rooty]
                smallest[rootx] = min(smallest[rootx], smallest[rooty])
                
        for i in range(len(s1)):
            union(s1[i], s2[i])

        res = []
        for ch in baseStr:
            res.append(smallest[find(ch)])
            
        return "".join(res)
        