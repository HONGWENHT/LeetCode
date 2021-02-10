from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        dp = [i for i in range(len(isConnected))]

        def find(a):
            while dp[a] != a:
                a = dp[a]
            return dp[a]

        def union(b, c):
            if find(b) != find(c):
                father = min(find(b), find(c))
                while dp[b] != father:
                    tmp = dp[b]
                    dp[b] = father
                    b = tmp
                while dp[c] != father:
                    tmp = dp[c]
                    dp[c] = father
                    c = tmp

        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                print(i, j)
                if isConnected[i][j]:
                    if find(i) != find(j):
                        union(i, j)

        ret = set()
        for i in range(len(isConnected)):
            ret.add(find(i))

        return len(ret)

s = Solution()
s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])