from typing import List


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        ret = [i for i in range(1, len(s) + 2)]
        i = 1
        while i < len(ret):
            j = i
            while i < len(ret) and s[i - 1] == 'D':
                i += 1
            ret[j-1:i] = ret[j-1:i][::-1]
            i += 1

        return ret

s = Solution()
s.findPermutation("DDIIDI")