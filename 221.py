from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        matrix = [list(map(int, m)) for m in matrix]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                val = matrix[r][c]
                if val == 1:
                    if r - 1 >= 0 and c - 1 >= 0 and matrix[r - 1][c] == matrix[r][c - 1] and matrix[r - 1][c - 1]:
                        matrix[r][c] = min(matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1]) + 1

        return pow(max(list(map(max, matrix))), 2)

s = Solution()
s.maximalSquare([["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]])
