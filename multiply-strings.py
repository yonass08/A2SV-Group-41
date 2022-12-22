class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))

        num1 = num1[::-1]
        num2 = num2[::-1]

        for i, digit1 in enumerate(num1):
            for j, digit2 in enumerate(num2):
                res[i+j] = res[i+j] + int(num1[i]) * int(num2[j]) 
                
        carry = 0
        for i in range(len(res)):
            carry += res[i]
            res[i] = carry % 10
            carry //= 10

        while res and res[-1] == 0:
            res.pop()

        res = res[::-1]

        return ''.join([str(x) for x in res]) or '0'

        
