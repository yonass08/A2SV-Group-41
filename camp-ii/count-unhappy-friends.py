class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pair = {}
        for a, b in pairs:
            pair[a] = b
            pair[b] = a
            
        pref = []
        for person in range(n):
            pref.append({})
            
            for i, num in enumerate(preferences[person]):
                pref[person][num] = i
                
        res = 0
        
        for person in range(n):
            pairp = pair[person]
            idx = pref[person][pairp]
            
            unhappy = 0
            for i in range(idx):
                pos = preferences[person][i]
                posp = pair[pos]
                
                if pref[pos][person] < pref[pos][posp]:
                    unhappy = 1
                    
            res += unhappy
                    
        return res
        