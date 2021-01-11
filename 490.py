from typing import List


class Solution:
    def go(self, maze, direction, x, y):
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        while True:
            if x + directions[direction][0] < 0 or x + directions[direction][0] >= len(maze) or y + \
                    directions[direction][1] < 0 or y + directions[direction][1] >= len(maze[0]) or \
                    maze[x + directions[direction][0]][y + directions[direction][1]] == 1:
                return (x, y)
            x, y = x + directions[direction][0], y + directions[direction][1]

    def DFS(self, cur, maze, visited, target):
        if self.ans == True:
            return
        if cur == target:
            self.ans = True
            return
        for i in range(4):
            nxt = self.go(maze, i, cur[0], cur[1])
            if nxt not in visited:
                visited.add(nxt)
                self.DFS(nxt, maze, visited, target)
                visited.remove(nxt)

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        self.ans = False
        self.DFS((start[0], start[1]), maze, visited, (destination[0], destination[1]))
        return self.ans


s = Solution()
s.hasPath(
[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],[0,4], [4,4])