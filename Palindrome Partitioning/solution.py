class Solution:
    def dfs(self, ret, s, start, curr, arr):
        if start >= len(s):
            ret.append(list(curr))
        for end in range(start, len(s)):
            if s[end] == s[start] and (end-start <= 2 or arr[start+1][end-1]):
                arr[start][end] = True
                curr.append(s[start:end+1])
                self.dfs(ret, s, end +1, curr, arr)
                curr.pop()
        
    def partition(self, s: str) -> List[List[str]]:
        l = len(s)
        arr = [[False for k in range(l)] for k in range(l)]
        ret = []
        self.dfs(ret, s, 0, [], arr)
        return ret
