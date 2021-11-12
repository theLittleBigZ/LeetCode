class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for n in range(1,10000):
            tot = n
            fail = False
            for m in nums:
                tot += m
                if tot<=0:
                    fail = True
                    break
            if not fail:
                return n
