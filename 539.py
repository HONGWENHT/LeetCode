from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if '00:00' in timePoints:
            timePoints.append('24.00')

        dp = []
        for item in timePoints:
            x = item.split(':')
            hour = x[0]
            minu = x[1]
            dp.append(hour * 100 + minu)

        dp.sort()

        ret = float('inf')

        for i in range(1, len(dp)):
            ret = min(dp[i] - dp[i - 1], ret)

        return ret


s  = Solution()
s.findMinDifference(["23:59","00:00"])