class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()
        if "inf" in s or "infinity" in s:
            return False
        try:
            val = float(s)
            return True
        except ValueError:
            return False
