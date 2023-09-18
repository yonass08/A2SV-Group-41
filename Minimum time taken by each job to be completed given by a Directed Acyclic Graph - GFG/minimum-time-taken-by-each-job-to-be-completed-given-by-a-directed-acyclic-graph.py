from typing import List
from collections import deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        seen = [False] * (n+1)
        incoming = [0] * (n+1)
        
        graph = [[] for _ in range(n+1)]
        res = [0] * n
        
        for left, right in edges:
            incoming[right] += 1
            graph[left].append(right)
            
        queue = deque()
        for node in range(1, n+1):
            if incoming[node] == 0:
                queue.append(node)
                seen[node] = True
                
        time = 1
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                res[curr-1] = time
                
                for child in graph[curr]:
                    if seen[child]:
                        continue
                    
                    incoming[child] -= 1
                    if incoming[child] == 0:
                        queue.append(child)
                        seen[child] = True
            time += 1
            
        return res



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends