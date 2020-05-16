# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/16 12:42
"""
42. 接雨水

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

[0,1,0,2,1,0,1,3,2,1,2,1]，在这种情况下，可以接 6 个单位的雨水.

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        q = []
        lh = 0
        res = 0
        for i in range(len(height)):
            while len(q)>0 and height[i] >= q[-1][0]:
                res += (i-q[-1][1]-1)*(q[-1][0]-lh)
                lh = q[-1][0]
                q.pop(-1)
            if len(q)>0:
                res += (i - q[-1][1] - 1) * (height[i] - lh)
            q.append((height[i], i))
            lh = height[i]
        return res


if __name__ == '__main__':
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
