class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        for l in range(int(math.ceil(len(num)/2))):
            if not num[l] == num[-(l+1)]:
                return False
        return True
