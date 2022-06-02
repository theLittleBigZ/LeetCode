class Solution:
    def romanToInt(self, s: str) -> int:
        conv = {
            "x":0,
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        ret = 0
        s = s +"x"
        for c in range(len(s)-1):
            if(conv[s[c]] < conv[s[c+1]]):
                ret -= conv[s[c]]
            else:
                ret += conv[s[c]]
            
        return ret
            
