from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic = {}
        for i, v in enumerate(intervals):
            dic[v[0]] = i
        copy = list(intervals)
        intervals = sorted(intervals, key=lambda x: x[0])

        def bs(left, right, target, intervals):
            while left <= right:
                mid = (left + right) // 2
                if intervals[mid][0] < target:
                    left = mid + 1
                elif intervals[mid][0] > target:
                    right = mid - 1
                else:
                    return intervals[mid]
            return intervals[left]

        ret = []
        for item in copy:
            start = bs(0, len(copy) - 1, item[1], intervals)
            if start == -1:
                ret.append(-1)
            else:
                result = dic[start]
                ret.append(result)
        return ret


s = Solution()
s.findRightInterval([[4,5],[2,3],[1,2]])
