import bisect


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        ans = []
        start_end = []
        dp = []

        for i in range(len(startTime)):
            start_end.append((startTime[i], endTime[i], profit[i]))
            dp.append(-1)

        start_end.sort()
        startTime.sort()

        def find_next(cur_end):
            return bisect.bisect_left(startTime, cur_end)

        def helper(idx):
            if idx == len(start_end):
                return 0

            if dp[idx] != -1:
                return dp[idx]

            cur_start = start_end[idx][0]
            cur_end = start_end[idx][1]
            cur_profic = start_end[idx][2]

            next_start = find_next(cur_end)

            ans = max(cur_profic + helper(next_start), helper(idx + 1))

            dp[idx] = ans
            return ans

        ans = 0
        helper(0)

        for item in dp:
            ans = max(max, item)

        return ans