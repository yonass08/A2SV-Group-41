class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLastChar = False

class Solution:
    def __init__(self):
        self.Trie = TrieNode()

    def idx(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        curr = self.Trie
        for ch in word:
            if curr.children[self.idx(ch)] == None:
                curr.children[self.idx(ch)] = TrieNode()
            curr = curr.children[self.idx(ch)]
        curr.isLastChar = True

    def longestWord(self, words: List[str]) -> str:
        for word in words:
            self.insert(word)

        res = []

        def dfs(Trie, word):
            nonlocal res
            if len(word) > len(res):
                res = word.copy()

            for idx, child in enumerate(Trie.children):
                if child == None:
                    continue
                    
                if child.isLastChar:
                    dfs(child, word + [chr(idx + ord('a'))])

        dfs(self.Trie, [])
        
        return "".join(res)



        
        
        