class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = {
            '0':0,
            '1':0,
            '2':0,
        }
        for n in nums:
            if n == 0:
                colors['0'] += 1
            elif n == 1:
                colors['1'] += 1
            else:
                colors['2'] += 1
        ret = ([0]*colors['0']) + [1]*colors['1'] + [2]*colors['2']
        nums.clear()
        for n in ret:
            nums.append(n)
