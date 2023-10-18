class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parent = list(range(n))
        parent[firstPerson] = 0
        
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
            if rootx == 0 or rooty == 0:
                parent[rootx] = 0
                parent[rooty] = 0
            else:
                parent[rooty] = rootx
                
        groups = defaultdict(list)
        for x, y, time in meetings:
            groups[time].append((x, y))
            
        for time in sorted(groups.keys()):
            for x, y in groups[time]:
                union(x, y)
                
            for x, y in groups[time]:
                if find(x) != 0:
                    parent[x] = x
                    parent[y] = y
                    
            # print(parent)
                    
        return [i for i in range(n) if find(i) == 0]
            
        