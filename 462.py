import random
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        def partition(lo, hi):
            pi = random.randint(lo, hi)
            nums[pi], nums[hi] = nums[hi], nums[pi]

            p = hi
            hi -= 1
            while lo <= hi:
                if nums[lo] < nums[p]:
                    lo += 1
                elif nums[hi] > nums[p]:
                    hi -= 1
                else:
                    nums[lo], nums[hi] = nums[hi], nums[lo]
                    lo += 1
                    hi -= 1
            nums[hi], nums[p] = nums[p], nums[hi]
            return hi

        lo, hi = 0, len(nums) - 1
        while True:
            mid = partition(lo, hi)
            if mid == len(nums) // 2:
                break
            elif mid > len(nums) // 2:
                hi = mid - 1
            else:
                lo = mid + 1

        return sum(abs(x - nums[mid]) for x in nums)


s = Solution()
s.minMoves2([1,2,3])