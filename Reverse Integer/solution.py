class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
        
        x = str(abs(x))
        x = x[::-1]
        x = int(x)
        
        if x < 2147483648:
            if neg:
                return x * -1
            return x
        return 0
