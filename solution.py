class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        def dfs(row, col):
            board[row][col] = "Z"
            for dr, dc in (-1, 0), (0, 1), (1, 0), (0, -1):
                nr, nc = row + dr, col + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or board[nr][nc] != 'O':
                    continue
                dfs(nr, nc)

        def flip():
            for row in range(rows):
                for col in range(cols):
                    if board[row][col] == "Z":
                        board[row][col] = "O"
                    elif board[row][col] == "O":
                        board[row][col] = "X"

        for row in [0, rows - 1]:
            for col in range(cols):
                if board[row][col] == 'O':
                    dfs(row, col)

        for col in [0, cols - 1]:
            for row in range(1, rows - 1):
                if board[row][col] == 'O':
                    dfs(row, col)

        flip()
