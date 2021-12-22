from numpy import log as ln
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        return ((ln(n)/ln(2)+1)/0.100).is_integer()
