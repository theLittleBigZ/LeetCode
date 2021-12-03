class Solution:
    def maxProduct(self, nums):
        res = [1, 1, nums[0]]
        for num in nums:
            val = (num, num*res[0], num*res[1])
            res[0] = min(val)
            res[1] = max(val)
            res[2] = max(res[2], res[1])
        return max(res)
