# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/25 21:33
"""
1524. 和为奇数的子数组数目

给你一个整数数组 arr 。请你返回和为 奇数 的子数组数目。

由于答案可能会很大，请你将结果对 10^9 + 7 取余后返回。



示例 1：

输入：arr = [1,3,5]
输出：4
解释：所有的子数组为 [[1],[1,3],[1,3,5],[3],[3,5],[5]] 。
所有子数组的和为 [1,4,9,3,8,5].
奇数和包括 [1,9,3,5] ，所以答案为 4 。

示例 2 ：

输入：arr = [2,4,6]
输出：0
解释：所有子数组为 [[2],[2,4],[2,4,6],[4],[4,6],[6]] 。
所有子数组和为 [2,6,12,4,10,6] 。
所有子数组和都是偶数，所以答案为 0 。

示例 3：

输入：arr = [1,2,3,4,5,6,7]
输出：16

示例 4：

输入：arr = [100,100,99,99]
输出：4

示例 5：

输入：arr = [7]
输出：1



提示：

    1 <= arr.length <= 10^5
    1 <= arr[i] <= 100
"""
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        mod = int(1e9 + 7)
        odd, even = 0, 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                odd, even = odd, even + 1
            else:
                odd, even = even + 1, odd
            res += odd
            res %= mod
        return res


if __name__ == '__main__':
    print(Solution().numOfSubarrays([1, 3, 5]), 4)
    print(Solution().numOfSubarrays([2, 4, 6]), 0)
    print(Solution().numOfSubarrays([1, 2, 3, 4, 5, 6, 7]), 16)
    print(Solution().numOfSubarrays([100, 100, 99, 99]), 4)
    print(Solution().numOfSubarrays([7]), 1)
