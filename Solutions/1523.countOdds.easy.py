# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/25 21:33
"""
1523. 在区间范围内统计奇数数目

给你两个非负整数 low 和 high 。请你返回 low 和 high 之间（包括二者）奇数的数目。



示例 1：

输入：low = 3, high = 7
输出：3
解释：3 到 7 之间奇数数字为 [3,5,7] 。

示例 2：

输入：low = 8, high = 10
输出：1
解释：8 到 10 之间奇数数字为 [9] 。



提示：

    0 <= low <= high <= 10^9
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            res = (high - low + 1) // 2
        else:
            res = (high - low) // 2 + 1
        return res


if __name__ == '__main__':
    print(Solution().countOdds(3, 7), 3)
    print(Solution().countOdds(8, 10), 1)
    print(Solution().countOdds(8, 11), 2)
    print(Solution().countOdds(8, 8), 0)
    print(Solution().countOdds(3, 5), 2)
    print(Solution().countOdds(3, 4), 1)
    print(Solution().countOdds(3, 3), 1)