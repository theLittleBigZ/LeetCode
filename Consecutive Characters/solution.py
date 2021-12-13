class Solution:
    def maxPower(self, s: str) -> int:
        cCount = 1
        maxCount = 0
        
        for x in range(1, len(s)):
            if s[x] == s[x-1]:
                cCount += 1
                maxCount = max(cCount, maxCount)
            else:
                cCount = 1
        return maxCount
