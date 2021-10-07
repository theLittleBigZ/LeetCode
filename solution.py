class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for x in range(len(nums)):
            find = target - nums[x]
            if find in cache:
                return [cache[find], x]
            else:
                cache[nums[x]] = x
