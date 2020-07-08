# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/8 16:58
"""
440. 字典序的第K小数字

给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。

注意：1 ≤ k ≤ n ≤ 109。

示例 :

输入:
n: 13   k: 2

输出:
10

解释:
字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
"""
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def getcount(pre):
            count = 0
            next = pre + 1
            while pre <= n:
                count += min(n+1, next) - pre
                pre *= 10
                next *= 10
            return count
        pre = 1
        while k != 1:
            count = getcount(pre)
            if count >= k:
                pre *= 10
                k -= 1
            else:
                pre += 1
                k -= count
        return pre


if __name__ == '__main__':
    print(
        Solution().findKthNumber(13, 2),
        Solution().findKthNumber(10, 3),
    )