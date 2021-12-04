class Trie:

    def __init__(self):
        self.chars, self.ends_here = defaultdict(Trie), False
    def insert(self, s):
        cur = self
        for c in reversed(s):
            cur = cur.chars[c]
        cur.ends_here = True
    def search(self, s):
        cur = self
        for c in s:
            if c not in cur.chars: return False
            cur = cur.chars[c]
            if cur.ends_here: return True
    
class StreamChecker:

    def __init__(self, words):
        self.trie = Trie()
        self.stream = deque()
        for letter in words:
            self.trie.insert(letter)

    def query(self, c):
        self.stream.appendleft(c)
        return self.trie.search(self.stream)
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
