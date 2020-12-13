import collections


class Ugly:
    def __init__(self):
        self.nums = [1, ]
        p2 = p3 = p5 = 0
        for i in range(1, 1690):
            ugly = min(self.nums[p2] * 2, self.nums[p3] * 3, self.nums[p5] * 5)
            self.nums.append(ugly)
            if ugly == self.nums[p2] * 2:
                p2 += 1
            elif ugly == self.nums[p3] * 3:
                p3 += 1
            elif ugly == self.nums[p5] * 5:
                p5 += 1


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        u = Ugly()
        return u.nums[n]

s = Solution()
s.nthUglyNumber(10)

s = "ffffannnssh"

print(collections.Counter(s))
