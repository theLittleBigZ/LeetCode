class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = []
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    que.append((i, j))
        adj = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        t = 0
        while que:
            f = 0
            for i in range(len(que)):
                u = que.pop(0)
                for v in adj:
                    if u[0]+v[0] > -1 and u[1]+v[1] > -1 and u[0]+v[0] < n and u[1]+v[1] < m and grid[u[0]+v[0]][u[1]+v[1]] == 1:
                        f = 1
                        grid[u[0]+v[0]][u[1]+v[1]] = 2
                        que.append((u[0]+v[0], u[1]+v[1]))
            t += f
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return t
