class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cache = {}
        dup = []
        for num in nums:
            if num in cache.keys():
                cache[num] += 1
            else:
                cache[num] = 0
        for key in cache.keys():
            if cache[key] > 0:
                dup.append(key)
        return dup
