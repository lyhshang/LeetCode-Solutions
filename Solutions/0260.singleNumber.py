# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/14 11:52
"""
260. 只出现一次的数字 III

给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]

注意：

    结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
    你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
"""
import sys
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xy = 0
        for num in nums:
            xy ^= num
        dif = xy & (-xy)
        x = 0
        for num in nums:
            if dif & num:
                x ^= num
        return [x, xy ^ x]


if __name__ == '__main__':
    print(Solution().singleNumber([1,2,1,2,3,5]))
