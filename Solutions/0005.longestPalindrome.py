"""
# 5. 最长回文子串

## 题意
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

**示例1:**
```
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
```
**示例2:**
```
输入: "cbbd"
输出: "bb"
```

## 题解
暴力遍历回文子串的中心和长度可以在O(n<sup>2</sup>)内解决，
利用回文串的对称性，可以优化到O(n)。

先向原串中插入"#"分隔符，这样就把最长回文子串统一到奇数长度，便于计算。

从左向右扫描，维护一个有最大右边界的回文子串中心`max_right`。
如果当前点在维护的右边界`max_right + l[max_right]`内，
则可以利用其关于回文子串中心的对称点的结果`l[max_right * 2 - i]`。
所有点会被遍历一次，右边界最多被拓展n次，所以时间复杂度是O(n)。

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ns = "#"
        for c in s:
            ns += c + "#"
        l = [0 for i in ns]
        max_right = 0
        res_index = 0
        for i in range(len(ns)):
            if i < max_right + l[max_right]:
                l[i] = min(l[max_right * 2 - i], max_right + l[max_right] - i)
            if i + l[i] >= max_right + l[max_right]:
                while i + l[i] + 1 < len(ns) and i - l[i] - \
                        1 >= 0 and ns[i + l[i] + 1] == ns[i - l[i] - 1]:
                    l[i] += 1
                max_right = i
                res_index = i if l[i] > l[res_index] else res_index
        res = ns[res_index - l[res_index] + 1:res_index + l[res_index]:2]
        return res


if __name__ == '__main__':
    print(
        Solution().longestPalindrome("babad"),
        Solution().longestPalindrome("cbbd"),
    )
