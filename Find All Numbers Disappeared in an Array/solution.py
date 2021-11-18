class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        return list(set(range(1, len(nums)+1)) - set(nums))
