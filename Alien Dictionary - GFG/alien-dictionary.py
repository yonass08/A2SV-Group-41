#User function Template for python3
from collections import defaultdict

class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        graph = defaultdict(list)
        single = set()
        
        for i in range(N-1):
            single.update(alien_dict[i])
            idx = 0
            
            while idx < len(alien_dict[i]) and idx < len(alien_dict[i+1]) \
            and alien_dict[i][idx] == alien_dict[i+1][idx]:
                idx += 1
                
            if idx < len(alien_dict[i]) and idx < len(alien_dict[i+1]):
                graph[alien_dict[i][idx]].append(alien_dict[i+1][idx])
        
                
        seen = set()
        res = []
        
        def dfs(letter):
            for child in graph[letter]:
                if child not in seen:
                    dfs(child)
                    
            res.append(letter)
            seen.add(letter)
        
        keys = list(graph.keys())
        for letter in keys:    
            if letter not in seen:
                dfs(letter)
            
        res.reverse()
        for letter in single:
            if letter not in seen:
                res.append(letter)
             
        return "".join(res)
                    
                
                
                
            
            
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends