class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for x in range(len(nums)):
            if target <= nums[x]:
                return x
        return len(nums)
