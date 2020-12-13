import math
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        if self.n == 0: return
        x = int(math.ceil(math.log2(self.n)))
        self.nums = nums
        self.tree = [0] * (2 * int(x ** 2) - 1)
        self.build(0, 0, self.n - 1)

    def build(self, index, start, end):
        if start == end:
            self.tree[index] = self.nums[start]
        else:
            mid = (start + end) // 2
            self.build(2 * index + 1, start, mid)
            self.build(2 * index + 2, mid + 1, end)
            self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def update(self, i: int, val: int) -> None:
        def helper(node, start, end, index, val):
            if start == end:
                self.nums[index] = val
                self.tree[node] = val
            else:
                mid = (start + end) // 2
                if index <= mid:
                    helper(2 * node + 1, start, mid, index, val)
                else:
                    helper(2 * node + 2, mid + 1, end, index, val)
                self.tree[node] = self.tree[2 * node + 2] + self.tree[2 * node + 1]

        helper(0, 0, self.n - 1, i, val)

    def sumRange(self, i: int, j: int) -> int:
        def query(node, start, end, l, r):
            if l > r: return 0
            if l == start and end == r:
                return self.tree[node]
            mid = (start + end) // 2
            return query(2 * node + 1, start, mid, l, min(r, mid)) + query(2 * node + 2, mid + 1, end, max(l, mid), r)

        return query(0, 0, self.n - 1, i, j)

s = NumArray([-1])
s.sumRange(0, 2)
s.update(1,2)
s.sumRange(0, 2)