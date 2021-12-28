class Solution:
    def frequencySort(self, s: str) -> str:
        hold = {}
        ret = ""
        for letter in s:
            if not hold.get(letter):
                hold[letter] = 0
            hold[letter] += 1
        hold = {k: v for k, v in sorted(hold.items(), key=lambda item: item[1], reverse=True)}
        for letter in hold.keys():
            ret += letter * hold[letter]
        return ret
