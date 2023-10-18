class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = list(range(len(strs)))
        size = [0] * len(strs)
        
        def areEquivalent(str1, str2):
            diff = 0
            
            for i in range(len(str1)):
                diff += str1[i] != str2[i]
                
                if diff > 2:
                    return False
                
            return True
            
        
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
            else:
                parent[rooty] = rootx
                size[rootx] += size[rooty]
                
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if areEquivalent(strs[i], strs[j]):
                    union(i, j)
                    
        return sum([int(parent[i] == i) for i in range(len(strs))])
                
        
        