from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i, v  in enumerate(nums):
            st = set ()
            flag = v > 0
            while i not in st:
                st.add(i)
                if (nums[i] > 0) != flag:
                    return False
                i = (i + nums[i]) % len(nums)
            return len(st) >= 1
        return False

s = Solution()
s.circularArrayLoop([2,-1,1,2,2])