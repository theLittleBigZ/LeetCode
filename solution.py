class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        ret = {}
        for puzzle in puzzles:
            ret[puzzle] = 0
            for word in words:
                if puzzle[0] in word:
                    puzzleC = set(list(puzzle))
                    wordC = set(list(word))
                    if wordC.issubset(puzzleC):
                        ret[puzzle] += 1
        return list(ret.values())
