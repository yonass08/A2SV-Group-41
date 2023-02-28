class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = '+-*/'
        stack = []
        
        switcher = {'+': (lambda x,y: y+x), '-': (lambda x,y: y-x), '*': (lambda x,y: y*x), '/': (lambda x,y: int(y/x)), }
        
        for i in tokens:
            if i in operations:
                temp = switcher[i](stack.pop(), stack.pop())
                stack.append(temp)    
            else:
                stack.append(int(i))
        
        return stack[0]
        
