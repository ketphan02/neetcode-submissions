class PrefixTree:
    
    WORD_END = "#"

    def __init__(self):
        self.head = {}

    def insert(self, word: str) -> None:
        cur = self.head
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        
        if self.WORD_END not in cur:
            cur[self.WORD_END] = True


    def search(self, word: str) -> bool:
        cur = self.head
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return self.WORD_END in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True

        
        