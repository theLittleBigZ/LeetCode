class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWords = 0
        for x in sentences:
            word = x.split()
            if len(word) > maxWords:
                maxWords = len(word)
        return maxWords
