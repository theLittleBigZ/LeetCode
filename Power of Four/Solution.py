class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        from math import log
        return log(n, 4).is_integer()
