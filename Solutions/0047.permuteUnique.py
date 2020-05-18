# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/18 22:02
"""
47. 全排列 II

给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        nums.sort()

        def dfs():
            if len(nums) == 0:
                res.append(temp.copy())
                return
            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                v = nums[i]
                nums.pop(i)
                temp.append(v)
                dfs()
                temp.pop(-1)
                nums.insert(i, v)

        dfs()
        return res


if __name__ == '__main__':
    print(
        Solution().permuteUnique([1,1,2]),
    )