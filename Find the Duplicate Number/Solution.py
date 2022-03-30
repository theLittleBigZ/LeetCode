class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashT = set()
        for x in nums:
            if x in hashT:
                return x
            hashT.add(x)
