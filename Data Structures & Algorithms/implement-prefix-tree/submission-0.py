class Node:
    def __init__(self, v):
        self.v = v
        self.hsh = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.head = Node("*")

    def insert(self, word: str) -> None:
        cur = self.head
        for c in word:
            if c not in cur.hsh:
                cur.hsh[c] = Node(c)
            cur = cur.hsh[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.head
        for c in word:
            if c not in cur.hsh:
                return False
            cur = cur.hsh[c]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for c in prefix:
            if c not in cur.hsh:
                return False
            cur = cur.hsh[c]
        return True
        