class Solution:
    def __init__(self):
        self.res = float('inf')

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k
        self.backtrack(cookies, children, 0)
        return self.res


    def backtrack(self, cookies, children, start):
        if start == len(cookies):
            self.res = min(self.res, max(children))
            return 

        for i in range(len(children)):
            children[i] += cookies[start]
            self.backtrack(cookies, children, start+1)
            children[i] -= cookies[start]
            
            if children[i] == 0:
                break
