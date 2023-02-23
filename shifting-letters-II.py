class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        total_shift = [0] * (len(s) + 1)

        for start, end, dirn in shifts:
            if dirn == 0:
                total_shift[start] -= 1
                total_shift[end+1] += 1
            else:
                total_shift[start] += 1
                total_shift[end+1] -= 1

        for idx in range(1, len(s)):
            total_shift[idx] += total_shift[idx-1]

        res = []
        for idx, char in enumerate(s):
            res.append(self.shift_char(char, total_shift[idx]))

        return ''.join(res)

    def shift_char(self, char, shift):
        index = (ord(char) + shift - 97) % 26
        return chr(index + 97)
