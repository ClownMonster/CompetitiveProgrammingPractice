# Trie Construction 

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = self.getNode()
    
    def getNode(self):
        return TrieNode()
    
    def _charToIndex(self, val):
        return ord(val)-ord('a')
        
    def insert(self,word):
        crawl = self.root
        for w in word:
            idx = self._charToIndex(w)
            if not crawl.children[idx]:
                crawl.children[idx] = self.getNode()
            crawl = crawl.children[idx]
            
        crawl.isEnd = True
            
    def search(self,word):
        crawl = self.root
        for w in word:
            idx = self._charToIndex(w)
            if not crawl.children[idx]:
                return False
            crawl = crawl.children[idx]
        return crawl.isEnd
        
if __name__ == "__main__":
    trie = Trie()
    trie.insert("mohan")
    print(trie.search("mohan"))
    
            
    
    
        
