# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/2 16:18
"""
60. 第k个排列

给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

给定 n 和 k，返回第 k 个排列。

说明：

    给定 n 的范围是 [1, 9]。
    给定 k 的范围是[1,  n!]。

示例 1:

输入: n = 3, k = 3
输出: "213"

示例 2:

输入: n = 4, k = 9
输出: "2314"
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        p = {0: 1}
        for i in range(1, n):
            p[i] = p[i - 1] * i

        k -= 1
        res = ""
        for i in range(n):
            pn = p[len(nums) - 1]
            index = k // pn
            res += nums[index]
            nums.pop(index)
            k %= pn
        return res


if __name__ == '__main__':
    print(
        Solution().getPermutation(n=3, k=3), "213",
        Solution().getPermutation(n=4, k=9), "2314",
    )
