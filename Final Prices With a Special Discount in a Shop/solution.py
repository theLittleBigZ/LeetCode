class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ret = []
        for i in range(len(prices)):
            ret.append(prices[i])
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    ret[i] -= prices[j]
                    break
        return ret
