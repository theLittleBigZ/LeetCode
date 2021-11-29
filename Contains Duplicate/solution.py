class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        print(counter, max(counter, key=counter.get))
        if counter[max(counter, key=counter.get)] >= 2:
            return True
        return False
