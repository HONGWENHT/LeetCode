class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        tollerance = 1
        if len(s) != len(t):
            less, more = '', ''
            if len(s) < len(t):
                less, more = s, t
            else:
                less, more = t, s

            p1 = p2 = 0

            while p1 < len(less):
                if tollerance == 1 and less[p1] != more[p2]:
                    p2 += 1
                    tollerance -= 1
                if tollerance == 0 and less[p1] != more[p2]:
                    return False
                p1 += 1
                p2 += 1
        else:
            for p in range(len(s)):
                if s[p] != t[p]:
                    if tollerance == 1:
                        tollerance -= 1
                        continue
                    else:
                        return False
        return tollerance == 0

s = Solution()
s.isOneEditDistance("a", "")