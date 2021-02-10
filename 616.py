from typing import List


class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        trie, intervals = {}, []

        for s in dict:
            cur = trie
            for c in s:
                cur = cur.setdefault(c, {})
            cur['#'] = 1

        print(trie)

        def addIntervals(interval):
            if intervals and intervals[-1][1] >= interval[0]:
                if intervals[-1][1] < interval[1]:
                    intervals[-1][1] = interval[1]
                else:
                    intervals.append(interval)

        for i in range(len(s)):
            cur, max_end = trie, None
            for j in range(i, len(s)):
                if s[j] not in cur:
                    break
                cur = cur[s[j]]
                if '#' in cur:
                    max_end = j + 1

            if max_end:
                addIntervals([i, max_end])

        ret = ''
        pre_end = 0
        print(intervals)
        for start, end in intervals:
            print((start, end))

            ret += s[pre_end: start] + '<b>' + s[start: end] + '</b>'
            pre_end = end

        return ret + s[pre_end:]

s = Solution()
s.addBoldTag(
"abcxyz123",
["abc","123"])