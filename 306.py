class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3: return False

        def helper(s, q):

            if len(q) > 2:
                if int(q[-1]) != int(q[-2]) + int(q[-3]):
                    return False

            if len(s) == 0:
                return True

            for i in range(len(s)):
                cur = s[:i + 1]
                q.append(cur)
                if helper(s[i + 1:], q):
                    return True
                q.pop(-1)

            return False

        return helper(num, [])


s = Solution()
s.isAdditiveNumber("111")