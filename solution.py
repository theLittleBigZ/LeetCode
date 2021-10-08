class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cache = {}
        dup = []
        for num in nums:
            if num in cache.keys():
                dup.append(num)
            else:
                cache[num] = 0
        return dup
