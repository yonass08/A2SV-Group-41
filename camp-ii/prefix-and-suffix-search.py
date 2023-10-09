class WordFilter:

    def __init__(self, words: List[str]):
        self.d = {}
        for w in range(len(words)):
            word = words[w]
            
            for j in range(len(word)-1 , -1 , -1): # for suffix
                
                for i in range(len(word)): # for prefix
                    
                    currS = word[:i+1] + "#" + word[len(word)-j-1:]
                    self.d[currS] = w        # w = index 
                

    def f(self, prefix: str, suffix: str) -> int:
        if (prefix + "#" + suffix) not in self.d:
            return -1
        
        return self.d[(prefix + "#" + suffix)]