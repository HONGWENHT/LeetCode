from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return None

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.BFS(rooms, i, j)

    def BFS(self, rooms: List[List[int]], row: int, col: int):
        q = []
        di = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q.append((row, col))
        level = 1
        while q:
            tmp = []
            for cur in q:
                for d in di:
                    row, col = cur[0] + d[0], cur[1] + d[1]
                    if row >= 0 and row < len(rooms) and col >= 0 and col < len(rooms[0]) and rooms[row][col] != -1 and \
                            rooms[row][col] != 0:
                        rooms[row][col] = min(rooms[row][col], level)
                        tmp.append((row, col))
            q = tmp
            level += 1

s = Solution()
s.wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]])