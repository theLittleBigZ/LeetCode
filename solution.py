class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minN = 0
        tot = 0
        for num in nums:
            tot += num
            minN = min(minN, tot)
        return -minN + 1
