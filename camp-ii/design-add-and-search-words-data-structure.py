class WordDictionary:

    def __init__(self):
        self.d={}
        
    def addWord(self, word: str) -> None:
        cur=self.d
        if not self.search(word):
            for i in range(len(word)):
                if word[i] not in cur:
                    cur[word[i]]={}
                cur=cur[word[i]]
                
            cur["#"]={}    
        

    def search(self, word: str) -> bool:
        cur=self.d
        def rec(start,cur):
            if start>=len(word):
                if "#" in cur:
                    return True
                else:
                    return False
                
            if word[start]==".":
                for k,v in cur.items():
                    if rec(start+1,v):
                        return True
                return False
            elif word[start] in cur:
                if rec(start+1,cur[word[start]]):
                    return True
                
            else:
                return False
            
        return rec(0,cur)  
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)