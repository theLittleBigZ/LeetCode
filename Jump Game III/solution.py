#ashu25
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        def isValidMove(idx):
            # to check if a particular move is allowed or not
            if idx >= 0 and idx < len(arr):
                return True
            return False
        
        visited = set()
        
        def canReachHelper(start, end=0):
            # visited set to solve cycles
            if start in visited:
                return False
            
            # found valid solution
            if arr[start] == end:
                return True
            
            steps = arr[start]
            visited.add(start)
            
            
            # jump right side of array
            new_positive_move = start + steps
            # jump left side of array
            new_negative_move = start - steps
            
            if isValidMove(new_positive_move):
                if canReachHelper(new_positive_move):
                    # early return incase a path is found
                    return True
                
            if isValidMove(new_negative_move):
                return canReachHelper(new_negative_move)
            
        
        return canReachHelper(start)
