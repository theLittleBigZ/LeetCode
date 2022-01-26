class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        climb = 0
        
        while(climb < len(arr)-1 and arr[climb] < arr[climb + 1]):
            climb = climb + 1
        if climb == 0 or climb == len(arr)- 1:
            return False
        while(climb < len(arr)-1 and arr[climb] > arr[climb + 1]):
            climb = climb + 1
        if climb == len(arr)-1:
            return True
