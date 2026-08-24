class WordDictionary:
    WORD_END = "#"

    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        cur = self.tree
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur[self.WORD_END] = True

    def search(self, word: str) -> bool:
        def search_helper(word_idx, cur):
            if word_idx >= len(word):
                return self.WORD_END in cur

            c = word[word_idx]
            if c in cur:
                return search_helper(word_idx + 1, cur[c])
            if c != '.' and c not in cur:
                return False
            if c == '.':
                for key in cur.keys():
                    if key == self.WORD_END:
                        continue
                    if search_helper(word_idx + 1, cur[key]):
                        return True
            return False

        return search_helper(0, self.tree)

