class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        oddP, evenP = 0, 0
        for x in position:
            if x % 2 == 0:
                evenP += 1
            else:
                oddP += 1
        return min(oddP, evenP)
