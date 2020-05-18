# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/18 21:51
"""
46. 全排列

给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def dfs():
            if len(nums) == 0:
                res.append(temp.copy())
                return
            for i in range(len(nums)):
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
        Solution().permute([1,2,3])
    )