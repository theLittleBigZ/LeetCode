class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def get_mask(s):
            return reduce(lambda x, y: x|y, [1<<(ord(c) - 97) for c in s])
        
        ans, cnt = [0]*len(puzzles), Counter()
        for word in words: cnt[get_mask(word)] += 1

        for i, puzzle in enumerate(puzzles):
            mask = get_mask(puzzle[1:])
            addon = 1<<(ord(puzzle[0]) - 97)
            submask = mask
            while submask:
                ans[i] += cnt[submask|addon]
                submask = (submask - 1) & mask
            ans[i] += cnt[addon]
            
        return ans
