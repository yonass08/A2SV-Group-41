class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = defaultdict(int)
        for idx, char in enumerate(s):
            last_index[char] = idx
        found = set()

        stack = []
        for idx, char in enumerate(s):
            if char not in found:
                while stack and last_index[stack[-1]] > idx and char <= stack[-1]:
                    found.remove(stack.pop())

                stack.append(char)
                found.add(char)

        return ''.join(stack)
