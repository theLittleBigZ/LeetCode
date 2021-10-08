class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word): #None
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.end_node = 1
        
    def searchHelper(self, word):
        root = self.root
        for symbol in word:
            if symbol in root.children:
                root = root.children[symbol]
            else:
                return -1

        return 1 if root.end_node == 1 else 0  

    def search(self, word): #bool:
        return self.searchHelper(word) == 1

    def startsWith(self, prefix): #bool:
        return self.searchHelper(prefix) >= 0
