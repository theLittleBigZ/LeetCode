# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    
    
    def guessNumber(self, n: int) -> int:
        mid = 0
        start = 0
        end = n
        
        while(start <= end):
            mid = (start + end)//2
            
            if guess(mid) == 0:
                return mid
            
            if guess(mid) == -1:
                end = mid -1
            else:
                start = mid + 1
