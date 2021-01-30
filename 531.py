from typing import List


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        st = set()
        for i in range(len(picture)):
            count = 0
            st_tmp = set()
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    count += 1
                    st_tmp.add((i, j))
                if count == 2:
                    break
            if count == 1:
                st = st.union(st_tmp)


        for row, col in st:
            count = 0
            for i in range(len(picture)):
                if picture[i][col] == 'B':
                    count += 1
                    if count == 2:
                        st.remove((i, col))
                        break

        return len(st)

s = Solution()
s.findLonelyPixel([["W","B","W","W"],["W","B","B","W"],["W","W","W","W"]])