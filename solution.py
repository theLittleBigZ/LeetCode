import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        itr = -1
        sub = 1
        while n >= 0:
            n = n - sub
            sub += 1
            itr += 1
        return itr
