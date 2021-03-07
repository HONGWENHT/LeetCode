import collections
import functools
import heapq
from typing import List


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        last = n

        mp = collections.defaultdict(list)
        for edge in edges:
            mp[edge[0]].append((edge[1], edge[2]))
            mp[edge[1]].append((edge[0], edge[2]))

        print(mp)

        dist = [float('inf')] * (n + 1)
        dist[n]  = 0
        cur = n
        h = [(0, cur)]
        while len(h):
            currentDistance, cur = heapq.heappop(h)
            for neighbor, distance in mp[cur]:
                newDistance = currentDistance + distance
                if dist[neighbor] == float('inf') or dist[neighbor] > newDistance:
                    dist[neighbor] = newDistance
                    heapq.heappush(h, (newDistance, neighbor))

        print(dist)

        dist = { i : v for (i ,v) in enumerate(dist) if i != 0}

        print(dist)

        @functools.lru_cache(None)
        def helper(n):
            if n == 1:
                return 1
            else:
                ret = 0
                for neighbor, weight in mp[n]:
                    if dist[neighbor] > dist[n]:
                        ret += helper(neighbor)
                return ret

        return helper(last) % (10 ** 9 + 7)



Solution().countRestrictedPaths(5, [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]])
