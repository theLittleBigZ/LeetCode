class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for ele in range(1,len(nums)):
            nums[ele] = nums[ele] + nums[ele - 1]
        return nums
