"""
# 3. 无重复字符的最长子串

## 题意

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

**示例1:**
```
输入: "abcabcbb"
输出: 3
原因: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```
**示例2:**
```
输入: "bbbbb"
输出: 1
原因: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```
**示例3:**
```
输入: "pwwkew"
输出: 3
原因: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

## 题解
求最长不含重复字符子串的长度。
考虑以当前字符为串尾，求最长不含重复字符子串的长度，
该长度即从串尾反推一直到第一次出现重复字符。
从正向看，这个第一次出现重复字符的位置即所有字符倒数第二次出现中的最大位置。

因为只需扫描一遍，维护所有字符倒数第二次出现的位置中的最大值`max_second_last`，
维护`max_second_last`只需要维护所有字符最后一次出现的位置`last`即可，
当`last`更新时，旧值即倒数第二次出现的位置，更新`max_second_last`。

时间复杂度O(n)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1 for i in range(256)]
        max_second_last = -1
        res = 0
        for i in range(len(s)):
            max_second_last = max(max_second_last, last[ord(s[i])])
            last[ord(s[i])] = i
            res = max(res, i - max_second_last)
        return res


if __name__ == '__main__':
    print(
        Solution().lengthOfLongestSubstring("abcabcbb"),
        Solution().lengthOfLongestSubstring("bbbbb"),
        Solution().lengthOfLongestSubstring("pwwkew"),
    )
