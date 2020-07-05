# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/5 10:30
"""
5452. 判断能否形成等差数列

给你一个数字数组 arr 。

如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列 。

如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false 。



示例 1：

输入：arr = [3,5,1]
输出：true
解释：对数组重新排序得到 [1,3,5] 或者 [5,3,1] ，任意相邻两项的差分别为 2 或 -2 ，可以形成等差数列。

示例 2：

输入：arr = [1,2,4]
输出：false
解释：无法通过重新排序得到等差数列。



提示：

    2 <= arr.length <= 1000
    -10^6 <= arr[i] <= 10^6
"""
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != arr[i-1] - arr[i-2]:
                return False
        return True


if __name__ == '__main__':
    print(
        Solution().canMakeArithmeticProgression([1,2])
    )