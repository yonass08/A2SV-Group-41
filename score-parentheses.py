class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        
        for p in s:
            if p == '(':
                stack += [p, 0]
            else:
                val = 0
                while stack[-1] != '(':
                    val += stack.pop()
                nval = 2 * val
                if val == 0:
                    nval = 1
                stack.pop()
                stack.append(nval)

        return sum(stack)
