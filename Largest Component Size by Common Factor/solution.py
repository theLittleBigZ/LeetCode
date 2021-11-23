class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        parent=[i for i in range(1+max(nums))]

        def find(x):
            if parent[x]==x:
                return x
            parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            px=find(x)
            py=find(y)
            if px!=py:
                parent[py]=px

        for num in nums:
            for i in range(2,1+int(pow(num,0.5))):
                if num%i==0:
                    union(i,num)
                    union(num,num//i)

        maps={}
        for num in nums:
            pnum=find(num)
            maps[pnum]=maps.get(pnum,0)+1

        return max(maps.values())
