class Solution:
    def printVertically(self, s: str) -> List[str]:
        word_list = s.split()
        res = []

        length = max(len(word) for word in word_list)

        for col in range(length):
            vertical_word = []
            for word in word_list:
                if col < len(word):
                    vertical_word.append(word[col])
                else:
                    vertical_word.append(' ')

            while vertical_word[-1] == " ":
                vertical_word.pop()

            res.append("".join(vertical_word))

        return res
