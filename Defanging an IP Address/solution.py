class Solution:
    def defangIPaddr(self, address: str) -> str:
        num = address.split('.')
        ret = ""
        for b in num:
            ret += b
            ret += "[.]"
        return ret[:-3]
