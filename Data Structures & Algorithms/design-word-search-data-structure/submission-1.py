class Node:
    def __init__(self, c: str = None):
        self.c = c
        self.hsh = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        cur = self.head
        for c in word:
            if c not in cur.hsh:
                cur.hsh[c] = Node(c)
            cur = cur.hsh[c]
        cur.end = True

    def search(self, word: str) -> bool:
        def searchRecursively(cur, idx) -> bool:
            if idx >= len(word):
                return cur.end

            if word[idx] in cur.hsh:
                return searchRecursively(cur.hsh[word[idx]], idx + 1)
            
            if word[idx] == ".":
                for key in cur.hsh:
                    if searchRecursively(cur.hsh[key], idx + 1):
                        return True

            return False


        cur = self.head
        return searchRecursively(cur, 0)