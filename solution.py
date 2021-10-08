class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        for l in range(len(num)):
            if not num[l] == num[-(l+1)]:
                return False
        return True
