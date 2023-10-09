class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = {}
        for word in words:
            curr = trie 
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]
                if 'count' not in curr:
                    curr['count'] = 0
                curr['count'] += 1
                
        res = []
        for word in words:
            curr = trie
            count = 0
            for ch in word:
                curr = curr[ch]
                count += curr['count']
            res.append(count)
        return res