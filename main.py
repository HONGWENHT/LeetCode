from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        left, right, ret, opt = 0, 0, 0, '+'
        for c in s + '+':
            if c == ' ':
                continue
            if c.isdigit():
                right = right * 10 + int(c)
                continue
            if opt == '+':
                ret += left
                left = right
            elif opt == '-':
                ret += left
                left = -right
            elif opt == '*':
                left = left * right
            elif opt == '/':
                left = left // right
            right, opt = 0, c

        return ret + left

s = Solution()
s.calculate("14-3/2")