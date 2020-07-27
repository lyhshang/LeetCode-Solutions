# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/11 22:28
"""
1508. 子数组和排序后的区间和

给你一个数组 nums ，它包含 n 个正整数。你需要计算所有非空连续子数组的和，并将它们按升序排序，得到一个新的包含 n * (n + 1) / 2 个数字的数组。

请你返回在新数组中下标为 left 到 right （下标从 1 开始）的所有数字和（包括左右端点）。由于答案可能很大，请你将它对 10^9 + 7 取模后返回。



示例 1：

输入：nums = [1,2,3,4], n = 4, left = 1, right = 5
输出：13
解释：所有的子数组和为 1, 3, 6, 10, 2, 5, 9, 3, 7, 4 。将它们升序排序后，我们得到新的数组 [1, 2, 3, 3, 4, 5, 6, 7, 9, 10] 。下标从 le = 1 到 ri = 5 的和为 1 + 2 + 3 + 3 + 4 = 13 。

示例 2：

输入：nums = [1,2,3,4], n = 4, left = 3, right = 4
输出：6
解释：给定数组与示例 1 一样，所以新数组为 [1, 2, 3, 3, 4, 5, 6, 7, 9, 10] 。下标从 le = 3 到 ri = 4 的和为 3 + 3 = 6 。

示例 3：

输入：nums = [1,2,3,4], n = 4, left = 1, right = 10
输出：50



提示：

    1 <= nums.length <= 10^3
    nums.length == n
    1 <= nums[i] <= 100
    1 <= left <= right <= n * (n + 1) / 2
"""
from typing import List


class Solution:
    def rangeSum2(self, nums: List[int], n: int, left: int, right: int) -> int:
        temp = []
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                temp.append(s)
        temp.sort()
        res = 0
        mod = int(1e9 + 7)
        for i in range(left, right + 1):
            res += temp[i - 1]
            res %= mod
        return res

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = int(1e9 + 7)
        sums = [0 for i in range(n + 1)]
        for i in range(n):
            sums[i + 1] = sums[i] + nums[i]

        ssums = [0 for i in range(n + 1)]
        for i in range(n):
            ssums[i + 1] = ssums[i] + sums[i + 1]

        def get_index(v) -> int:
            j = 1
            res = 0
            for i in range(n):
                while j <= n and sums[j] - sums[i] <= v:
                    j += 1
                res += j - i - 1
            return res

        def ef_get_kth(k) -> int:
            left, right = 0, int(1e5)
            while left < right:
                m = (left + right) // 2
                if get_index(m) < k:
                    left = m + 1
                else:
                    right = m
            return left

        def get_ssums(k) -> int:
            num = ef_get_kth(k)
            res = 0
            cnt = 0
            j = 1
            for i in range(n):
                while j <= n and sums[j] - sums[i] < num:
                    j += 1
                res += ssums[j - 1] - ssums[i] - sums[i] * (j - i - 1)
                cnt += j - i - 1
            return res + (k - cnt)*num

        return (get_ssums(right) - get_ssums(left - 1)) % mod


if __name__ == '__main__':
    print(Solution().rangeSum([1, 2, 3, 4], 4, 1, 5), 13)
    print(Solution().rangeSum([1, 2, 3, 4], 4, 3, 4), 6)
    print(Solution().rangeSum([1, 2, 3, 4], 4, 1, 10), 50)
    print(Solution().rangeSum([100 for _ in range(1000)], 1000, 1, 500500), 716699888)
