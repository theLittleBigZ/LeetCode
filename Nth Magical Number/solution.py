class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod = 10**9 + 7
        lcm = a * b / self.gcd(a, b) # least common multiple
        
        lo, hi = min(a, b), max(a, b) * n
        while lo <= hi:
            mid = (lo + hi) // 2

            curN = mid // a + mid // b - mid // lcm
                
            if curN == n:
                res = mid - min(mid % a, mid % b) # adjust to magic number
                return res % mod
            
            if curN < n:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo % mod
    
    def gcd(self, a, b): # greatest common divisor
        while b > 0:
            temp, b = b, a % b
            a = temp
    
        return a
