class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for n in range(l):
            nums.append(nums[n])
        return nums
