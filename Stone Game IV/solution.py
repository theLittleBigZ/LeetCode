class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dyn = [False]*(n+1)
        
        for x in range(1, n+1):
            for y in range(1, int(x**0.5)+1):
                if dyn[x-y*y] == False:
                    dyn[x] = True
                    break
        return dyn[n]
