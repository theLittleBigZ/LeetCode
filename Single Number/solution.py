class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for x in range(len(nums)):
            if not (nums[x] in nums[:x] + nums[x+1:]):
                return nums[x]
        return None
