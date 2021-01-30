from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ret = [-1] * len(nums)
        st = []
        for i in range(2 * len(nums) - 1, -1, -1):
            while st and nums[i % len(nums)] >= st[-1]:
                st.pop()

            ret[i % len(nums)] = (-1 if len(st) == 0 else nums[st[-1]])
            st.append(i % len(nums))

        return ret

s = Solution()
s.nextGreaterElements([1,2,1])