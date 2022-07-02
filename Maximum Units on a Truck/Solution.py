class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        units = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        index = 0
        total = 0
        while truckSize > 0 and index < len(units):
            if units[index][0] > 0:
                units[index][0] = units[index][0] - 1
                total = total + units[index][1]
                truckSize = truckSize - 1
            else:
                index = index + 1
            #print(units, total, index)
        return total
