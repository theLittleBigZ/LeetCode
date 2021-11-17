class Solution(object):
    def removeElement(self, nums, val):
        pos = 0
        for x in nums:
            if x != val:
                nums[pos] = x
                pos += 1
        return pos
