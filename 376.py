from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 2: return len(nums)
        ret = 1
        flag = None
        for i in range(1, len(nums)):
            if flag is None:
                if nums[i] > nums[i -1]:
                    flag = True
                    ret += 1
            elif flag is not None and (nums[i] > nums[i - 1]) is not flag:
                ret += 1
                flag = not flag
            else:
                continue

        return ret

s = Solution()
s.wiggleMaxLength([0,0])