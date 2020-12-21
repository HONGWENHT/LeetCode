class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        num = ''
        for i in s:
            if i.isdigit():
                num += i
            else:
                if num != '':
                    st.append(num)
                    num = ''
                if i != ']':
                    st.append(i)
                else:
                    tmp = ''
                    while st[-1] != '[':
                        tmp = st.pop() + tmp
                    st.pop()
                    count = int(st.pop())
                    for _ in range(count):
                        tmp += tmp
                    st.append(tmp)

        return ''.join(st)

s = Solution()
s.decodeString("3[a]2[bc]")