class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        complete = range(1, len(nums)+1)
        nums.sort()
        return list(set(complete) - set(nums))
