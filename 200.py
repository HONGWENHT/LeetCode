from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid: List[List[str]], col: int, row: int):
            dire = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            grid[row][col] = 'S'
            for d in dire:
                row += d[0]
                col += d[1]
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == '1':
                    dfs(grid, col, row)

        ret = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                val = grid[r][c]
                if val == '1':
                    dfs(grid, c, r)
                    ret += 1

        return ret

s = Solution()
s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])