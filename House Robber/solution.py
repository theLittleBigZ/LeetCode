class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        value = [0]*len(nums)
        value[0] = nums[0]
        value[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            value[i] = max(nums[i]+value[i-2], value[i-1])
        return value[-1]
