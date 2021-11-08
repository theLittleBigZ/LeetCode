class Solution:
    def binCof(self, n, m):
        ret = 1
        if m > (n - m):
            m = n - m
        for i in range(m):
            ret *= (n - i)
            ret //= (i + 1)
        return ret
        
    def numTrees(self, n: int) -> int:
        c = self.binCof(2 * n, n)
        return c // (n + 1)
