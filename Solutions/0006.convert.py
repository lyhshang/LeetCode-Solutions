"""
# 6. Z 字形变换

## 题意
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
```
L   C   I   R
E T O E S I I G
E   D   H   N
```
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：`"LCIRETOESIIGEDHN"`。

**示例1:**
```
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
```
**示例2:**
```
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
原因:
        L     D     R
        E   O E   I I
        E C   I H   N
        T     S     G
```
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        heads = ["" for i in range(numRows)]
        part = numRows * 2 - 2
        for i in range(len(s)):
            num = i % part
            j = num if num < numRows else part - num
            heads[j] += s[i]
        res = ""
        for i in range(len(heads)):
            res += heads[i]
        return res


if __name__ == '__main__':
    print(
        Solution().convert("LEETCODEISHIRING", 3),
        Solution().convert("LEETCODEISHIRING", 4),
    )
