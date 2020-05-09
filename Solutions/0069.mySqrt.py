# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/9 21:48
"""
69. x 的平方根

实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2

示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
"""
class Solution:
    # 二分查找法
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = -1
        while l<=r:
            m = (l+r)//2
            if m*m <= x:
                res = m
                l = m+1
            else:
                r = m-1
        return res

    # 牛顿法
    def mySqrt2(self, x: int) -> int:
        x0 = x
        while True:
            # 0 = y1 = 2x0(x1-x0)+y0 = 2x0(x1-x0)+x0*x0-x
            x1 = 0.5*(x0+x/x0)
            if abs(x1 - x) < 1e-7:
                break
            x0 = x1
        return int(x0)
