class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        a.sort()
        ans=[]
        i=0
        if(len(a)<3):
            return []
        while(i<len(a)-2):
            left=i+1
            right=len(a)-1
            while(left<right):
                if(a[i]+a[left]+a[right]==0):
                    ans.append([a[i],a[left],a[right]])
                    while(left<len(a)-1):
                        if(a[left]==a[left]+1):
                            left=left+1
                        else:
                            break
                    left=left+1
                    while(right>i):
                        if(a[right]==a[right-1]):
                            right=right-1
                        else:
                            break
                    right=right-1
                elif(a[i]+a[left]+a[right]<0):
                    left=left+1
                else:
                    right=right-1
            while(i<len(a)-1):
                if(a[i]==a[i+1]):
                    i=i+1
                else:
                    break
            i=i+1
        return ans
