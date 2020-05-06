import numpy


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = numpy.zeros((len(s) + 1, len(p) + 1))
        dp[0, 0] = 1
        for i in range(len(s) + 1):
            for j in range(1, len(p) + 1):
                if j >= 2 and p[j - 1] == '*':
                    if dp[i, j - 2] == 1:
                        dp[i, j] = 1
                    elif i >= 1 and dp[i - 1, j] == 1 and (s[i - 1] == p[j - 2] or p[j - 2] == '.'):
                        dp[i, j] = 1
                elif i >= 1:
                    if dp[i - 1, j -
                          1] == 1 and (s[i - 1] == p[j - 1] or p[j - 1] == '.'):
                        dp[i, j] = 1
        return dp[len(s), len(p)] == 1


if __name__ == '__main__':
    print(
        Solution().isMatch("aa", "a"), False,
        Solution().isMatch("aa", "a*"), True,
        Solution().isMatch("ab", ".*"), True,
        Solution().isMatch("aab", "a*a*b"), True,
        Solution().isMatch("mississippi", "mis*is*p*."), False,
    )
