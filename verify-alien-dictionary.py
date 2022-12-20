class Solution:
    def isGreater(self, word1, word2, order):
        for i in range(len(word1)):
            if i == len(word2):
                return True
            if word1[i] != word2[i]:
                return order[word1[i]] > order[word2[i]]
        return False

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        newOrder = {}
        for i, ch in enumerate(order):
            newOrder[ch] = i

        for i in range(len(words)-1):
            if self.isGreater(words[i], words[i+1], newOrder):
                return False
        return True
