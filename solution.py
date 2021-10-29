import itertools

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hold = []
        finished = True
        posX = 0
        posY = 1
        posZ = 2
        if len(nums) >= 3:
            for x in nums[:-2]:
                for y in nums[1:-1]:
                    for z in nums[2:]:
                        if posX == posY or posX == posZ or posY == posZ:
                            break
                        elif x + y + z == 0:
                            temp = [x,y,z]
                            temp.sort()
                            #print(temp, posX, posY, posZ)
                            if not temp in hold:
                                hold.append(temp)
                        posZ += 1
                    posY += 1
                    posZ = 2
                posX += 1
                posY = 1
        return hold
