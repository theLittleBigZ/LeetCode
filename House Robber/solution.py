class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        value = [0]*n
        value[0] = nums[0]
        value[1] = max(nums[0], nums[1])
        for i in range(2, n):
            value[i] = max(nums[i]+value[i-2], value[i-1])
        return value[-1]
