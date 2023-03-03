class Solution:
    def decodeString(self, s: str) -> str:
        if s.isdigit():
            return ''
        stack = []
        
        for char in s:
            if char == ']':
                string = []
                while stack[-1] != '[':
                    string.append(stack.pop())

                stack.pop()
                string = (''.join(reversed(string))) * stack.pop()
                stack.append(string)
            elif char.isdigit():
                last = 0
                if stack and str(stack[-1]).isdigit():
                    last = stack.pop()
                stack.append(last*10 + int(char))

            else:
                stack.append(char)

        return ''.join(stack)
