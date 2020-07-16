# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/16 18:56
"""
128. 最长连续序列

给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for k in s:
            if k-1 not in s:
                t = k + 1
                while t in s:
                    t += 1
                res = max(res, t-k)
        return res


if __name__ == '__main__':
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
