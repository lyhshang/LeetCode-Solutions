# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/11 10:04
"""
binarySearch
二分查找
log(n)从有序序列中找到目标索引
"""
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m
    return l