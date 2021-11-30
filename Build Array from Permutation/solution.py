class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ret = []
        for num in nums:
            ret.append(nums[num])
        return ret
