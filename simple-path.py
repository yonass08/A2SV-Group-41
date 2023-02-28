class Solution:
    def simplifyPath(self, path: str) -> str:
        path += '/'
        start = 1
        stack = []

        for i in range(len(path)):
            if path[i] == '/':
                curr = path[start: i]
                if curr == '' or curr == '.':
                    start = i+1
                    continue
                if stack and curr == '..':
                    stack.pop()
                if curr != '..':
                    stack.append(curr)
                start = i+1
            print(stack)


        return '/' + '/'.join(stack)

        
        
