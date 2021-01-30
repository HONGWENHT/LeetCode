import itertools
from typing import List


class Solution:
    def findBlackPixel(self, picture: List[List[str]], N: int) -> int:
        rows = []
        cols = []
        for i in range(len(picture)):
            if picture[i].count('B') == N:
                rows.append(i)
        for j in range(len(picture[0])):
            count = 0
            for i in range(len(picture)):
                if picture[i][j] == 'B':
                    count += 1

            if count == N:
                cols.append(j)

        points = list(itertools.product(rows, cols))
        ret = 0
        li = []
        for x, y in points:
            if picture[x][y] == 'B':
                ret += 1
                li.append((x, y))
        return ret

s = Solution()
s.findBlackPixel([["W","B","W","B","B","W"],["B","W","B","W","W","B"],["W","B","W","B","B","W"],["B","W","B","W","W","B"],["W","W","W","B","B","W"],["B","W","B","W","W","B"]], 3)