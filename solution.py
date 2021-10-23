class Solution:
    def rotate(self, nums: List[int]) -> int:
        return [nums[-1]] + nums[:-1]
    def findMin(self, nums: List[int]) -> int:
        low = nums[0]
        for n in range(len(nums)):
            if nums[0] < low:
                low = nums[0]
            nums = self.rotate(nums)
        return low
