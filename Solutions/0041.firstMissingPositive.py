# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/16 11:13
"""
41. 缺失的第一个正数

给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。



示例 1:

输入: [1,2,0]
输出: 3

示例 2:

输入: [3,4,-1,1]
输出: 2

示例 3:

输入: [7,8,9,11,12]
输出: 1


提示：

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ln = len(nums)
        hasone = False
        for i in range(ln):
            if nums[i] == 1:
                hasone = True
            elif nums[i] <= 0 or nums[i] > ln:
                nums[i] = 1
        if not hasone:
            return 1
        for i in range(ln):
            index = abs(nums[i])-1
            if nums[index] > 0:
                nums[index] = -nums[index]
        for i in range(ln):
            if nums[i] > 0:
                return i+1
        return ln + 1


if __name__ == '__main__':
    print(Solution().firstMissingPositive([3,4,-1,1]))
