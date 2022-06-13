class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1, len(triangle)):
            for element in range(row+1):
                triangle[row][element] += min(triangle[row-1][element-(element==row)],
                                      triangle[row-1][element-(element>0)])
        return min(triangle[-1])
