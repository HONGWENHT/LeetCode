from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [[0] * (len(nums) + 1) for _ in range(len(nums) + 1)]
        for s in range(len(nums), -1, -1):
            for e in range(s + 1, len(nums)):
                dp[s][e] = max(nums[s] - dp[s + 1][e], nums[e] - dp[s][e - 1])

        return dp[0][len(nums) - 1] < 0


s = Solution()
s.PredictTheWinner([1,5,2])