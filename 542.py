from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return None
        R = len(matrix)
        C = len(matrix[0])

        ret = [[float('inf')] * C for _ in range(R)]

        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def helper(o_i, o_j, ret, i, j, cur, visited):
            if (i, j) in visited:
                return
            if (i, j) != (o_i, o_j) and matrix[i][j] == 0:
                return
            else:
                ret[i][j] = min(ret[i][j], cur)
                visited.add((i, j))
                for rr, cc in dirs:
                    if 0 <= i + rr < R and 0 <= j + cc < C:
                        helper(o_i, o_j, ret, i + rr, j + cc, cur + 1, visited)

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    helper(i, j, ret, i, j, 0, set())

        return ret

s = Solution()
s.updateMatrix([[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]])
