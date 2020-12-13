from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for i , v in enumerate(reversed(citations)):
            if i + 1 <= v :
                return i + 1
        return 0

s = Solution()
s.hIndex([3,0,6,1,5])
