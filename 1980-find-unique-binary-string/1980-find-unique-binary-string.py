class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def toNum(s):
            num = 0
            for bit in s:
                num = num * 2 + int(bit)
                
            return num
        
        def toStr(num):
            res = []
            while num:
                res.append(str(num % 2))
                num //= 2
                
            res += ["0"] * (len(nums) - len(res))
            res.reverse()
            return "".join(res)
            
        
        numbers = sorted(map(toNum, nums))
        
        res = 0
        
        for num in numbers:
            if res != num:
                return toStr(res)
            res += 1
            
        return toStr(res)
        