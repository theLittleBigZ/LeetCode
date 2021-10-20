class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split(" ")
        words = words[::-1]
        ret = ""
        for x in words:
            if not (x == " " or x == ""):
                ret += x
                ret += " "
        return ret.strip()
            
