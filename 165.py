class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        l1, l2 = len(v1), len(v2)
        turn = 1 if l1 <= l2 else -1
        less = v1 if l1 <= l2 else v2
        more = v2 if l2 > l1 else v1
        p = 0
        for i in range(len(less)):
            num1 = int(less[i])
            num2 = int(more[i])
            if num1 > num2 :
                return 1 * turn
            elif num1 < num2:
                return -1 * turn
            p += 1
        while p < len(more):
            if int(more[p]) > 0:
                return -1 * turn
            p += 1
        return 0

s = Solution()
s.compareVersion("0.1", "1.1")