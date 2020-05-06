from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keys = [
            "_",
            "!@#",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"]
        res = []

        def dfs(numbers, letters):
            if numbers == "":
                res.append(letters)
            else:
                for c in keys[int(numbers[0])]:
                    dfs(numbers[1:], letters + c)
        if digits != "":
            dfs(digits, "")
        return res


if __name__ == '__main__':
    print(
        Solution().letterCombinations("23"), [
            "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
    )
