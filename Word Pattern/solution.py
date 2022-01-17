class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lis = s.split(' ')
        dic = {}
        
        if not len(pattern) == len(lis):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in dic and not dic[pattern[i]] == lis[i]:
                return False
            elif pattern[i] not in dic and lis[i] in dic.values():
                return False
            elif pattern[i] not in dic:
                dic[pattern[i]] = lis[i]
        return True
