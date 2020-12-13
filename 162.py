from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 : return 0
        left, right = 0, len(nums)
        while left < right :
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left

s = Solution()
s.findPeakElement([2,1])