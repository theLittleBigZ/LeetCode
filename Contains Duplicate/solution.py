class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        
        for key,value in counter.items():
            if value >= 2:
                return True
        return False
