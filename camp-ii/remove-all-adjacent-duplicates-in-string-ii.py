class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [[s[0], 1]]
        for i in range(1, len(s)):
            if stack and s[i] == stack[-1][0]:
                char, count = stack[-1][0], stack[-1][1]
                stack.append([char, count + 1])
                if stack[-1][1] == k:
                    for _ in range(k):
                        stack.pop()
            else:
                stack.append([s[i], 1])
                
        return "".join(element[0] for element in stack)