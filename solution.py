class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = end = None
        visit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    visit.add((i, j))
                elif grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                    visit.add((i, j))
        def backtrack(x, y, visit):
            if (x, y) == end:
                return len(visit) == 0
            result = 0
            if (x-1, y) in visit:
                visit.remove((x-1, y)) 
                result += backtrack(x-1, y, visit)  
                visit.add((x-1, y))  
            if (x+1, y) in visit:
                visit.remove((x+1, y))
                result += backtrack(x+1, y, visit)
                visit.add((x+1, y))
            if (x, y-1) in visit:
                visit.remove((x, y-1))
                result += backtrack(x, y-1, visit)
                visit.add((x, y-1))
            if (x, y+1) in visit:
                visit.remove((x, y+1))
                result += backtrack(x, y+1, visit)
                visit.add((x, y+1))
            return result
        return backtrack(start[0], start[1], visit)
