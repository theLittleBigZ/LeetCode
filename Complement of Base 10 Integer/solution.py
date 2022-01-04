class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binN ="{0:b}".format(n)
        new = ""
        for x in binN:
            if x == "1":
                new += "0"
            else:
                new += "1"
        return int(new, 2)
