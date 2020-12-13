from typing import List


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        pivot = -b / (2 * a)
        print(pivot)

        def count(x):
            return a * x * x + b * x + c

        left, right = 0, len(nums) - 1
        ret = []
        while left <= right:
            if abs(left - pivot) > abs(right - pivot):
                ret.append(count(nums[left]))
                left += 1
            else:
                ret.append(count(nums[right]))
                right -= 1

        if a > 0:
            ret.reverse()

        return ret

s = Solution()
s.sortTransformedArray([-4,-2,2,4],1,3, 5)