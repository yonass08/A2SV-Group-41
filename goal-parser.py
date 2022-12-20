class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        res = []
        while i < len(command):
            if command[i] == '(':
                if command[i+1] == ')':
                    res.append('o')
                    i += 2
                else:
                    res.append('al')
                    i += 4
            else:
                res.append('G')
                i += 1
        return ''.join(res)
