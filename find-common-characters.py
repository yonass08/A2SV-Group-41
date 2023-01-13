class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_counter = [0] * 26

        for char in words[0]:
            common_counter[ord(char) - ord('a')] += 1

            
        for i in range(1, len(words)):
            #current_counter = Counter(words[i])

            current_counter = [0] * 26

            for char in words[i]:
                current_counter[ord(char) - ord('a')] += 1

            for idx in range(26):
                common_counter[idx] = min(common_counter[idx], current_counter[idx])

        common_letters = []
        for idx, item in enumerate(common_counter):
            if(item > 0):
                common_letters += (chr(idx + ord('a'))) * item

        return common_letters
