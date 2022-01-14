class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        result = 0
        ranges = []
        for i in range(len(points)):
            intersect = None            
            for j in reversed(range(len(ranges))):
				# ranges have order, if last range lower than current point we dont need to check others
                if ranges[j][1] < points[i][0]: break
                
				# Try to find intersection
                intersect = self.intersection(ranges[j], points[i])
                if not intersect: continue
                
				# if we found intersection update range and break loop
                ranges[j] = intersect
                break
            
			# Increment counnter and save range
            if not intersect:
                ranges.append(points[i])
                result += 1

        return result
        
    def intersection(self, a, b):
        if a[0] > b[0]: a, b = b, a
            
        if a[0] <= b[0] and (a[1] in range(b[0], b[1] + 1)) or (a[1] >= b[1]):
            return [b[0], min(b[1], a[1])]
        
        return None
