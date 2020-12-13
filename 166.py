class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        ans = ''
        if bool(numerator < 0) != bool(denominator < 0):
            ans += '-'

        numerator, denominator = abs(numerator), abs(denominator)

        q = numerator // denominator
        r = numerator % denominator
        ans += str(q)
        h = {}
        if r != 0:
            ans += '.'
            while r != 0:
                if r in h:
                    l = h[r]
                    ans = ans[:l] + "(" + ans[l:] + ")"
                    break
                h[r] = len(ans)
                r *= 10
                ans += str(r // denominator)
                r %= denominator
        return ans

s = Solution()
s.fractionToDecimal(-50, 8)