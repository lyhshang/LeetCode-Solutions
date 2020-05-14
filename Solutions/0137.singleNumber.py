# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/14 11:36
"""
137. 只出现一次的数字 II

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3

示例 2:

输入: [0,1,0,1,0,1,99]
输出: 99
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        appear_once = appear_twice = 0
        for num in nums:
            appear_once = ~appear_twice & (appear_once ^ num)
            appear_twice = ~appear_once & (appear_twice ^ num)
        return appear_once


if __name__ == '__main__':
    print(Solution().singleNumber([1,3,1,3,1,3,2]))