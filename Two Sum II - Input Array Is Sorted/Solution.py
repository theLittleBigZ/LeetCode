class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x = 0 
        y = len(numbers)-1
        
        while numbers[x] + numbers[y] != target:
            s = numbers[x] + numbers[y]
            if s > target:
                y = y -1
            else:
                x = x + 1
        return [x+1, y+1]
            
