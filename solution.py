class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split(" ")
        words = words[::-1]
        words = list(filter(None, words))
        words = " ".join(words)
        return words
