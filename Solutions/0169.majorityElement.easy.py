# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/31 20:21
"""
169. 多数元素

给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。



示例 1:

输入: [3,2,3]
输出: 3

示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for num in nums:
            if res == num:
                count += 1
            elif count > 0:
                count -= 1
            else:
                count = 1
                res = num
        return res


if __name__ == '__main__':
    print(Solution().majorityElement([3, 2, 3]), 3)
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)
