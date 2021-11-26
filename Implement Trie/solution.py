class Trie:

    def __init__(self):
        self. root = {}
        self.end = False

    def insert(self, word: str) -> None:
        root = self.root
        for letter in word:
            if letter not in root:
                root[letter] = {}
            root = root[letter]
        root['end'] = 'end'

    def search(self, word: str) -> bool:
        root = self.root
        for letter in word:
            if letter not in root:
                return False
            root = root[letter]
        if 'end' in root:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for letter in prefix:
            if letter not in root:
                return False
            root = root[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
