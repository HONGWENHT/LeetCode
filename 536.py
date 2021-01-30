class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> TreeNode:

        if not s:
            return None

        if not '(' in s:
            return TreeNode(int(s))

        left_left = s.index('(')
        st = ['(']
        index = [left_left]
        for i in range(left_left + 1, len(s)):
            if s[i] == '(':
                st.append('(')
            elif s[i] == ')':
                st.pop()

            if len(st) == 0:
                index.append(i)
                break



        left_s = s[index[0] + 1: index[1]]
        right_s = None
        if index[1] + 1 != len(s):
            right_s = s[index[1] + 2: -1]

        cur = TreeNode(int(s[:index[0]]))
        cur.left = self.str2tree(left_s)
        cur.right = self.str2tree(right_s)

        return cur

s = Solution()
s.str2tree("4(2(3)(1))(6(5))")