import numpy as np
class Solution:    
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxA = -1
        for acc in accounts:
            temp = np.sum(acc)
            if temp > maxA:
                maxA = temp
        return maxA
