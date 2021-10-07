class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            find = target - nums[x]
            holder = nums.copy()
            holder[x] = "a"
            if find in holder:
                return [x, holder.index(find)]
