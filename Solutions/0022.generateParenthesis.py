from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n == 0:
            return res

        def dfs(k, r, letters):
            if k == 0 and r == 0:
                res.append(letters)
            else:
                if k > 0:
                    dfs(k - 1, r + 1, letters + '(')
                if r > 0:
                    dfs(k, r - 1, letters + ')')
        dfs(n, 0, "")
        return res


if __name__ == '__main__':
    print(
        Solution().generateParenthesis(3), [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
        ],
    )
