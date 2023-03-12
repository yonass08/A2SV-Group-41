class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        return self.backtrack(num, 0, [])

    
    def backtrack(self, num, start, curr):

        if len(curr) >= 3 and start == len(num):
            return True

        for i in range(start+1, len(num)+1):
            val = int(num[start: i])
            if len(curr) < 2 or curr[-2] + curr[-1] == val:
                if i - start > 1 and num[start] == '0':
                    continue
                curr.append(val)
                if self.backtrack(num, i, curr):
                    return True
                curr.pop()

        return False
            
        
