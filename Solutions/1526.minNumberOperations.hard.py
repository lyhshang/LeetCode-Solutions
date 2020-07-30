# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/25 21:33
"""
1526. 形成目标数组的子数组最少增加次数

给你一个整数数组 target 和一个数组 initial ，initial 数组与 target  数组有同样的维度，且一开始全部为 0 。

请你返回从 initial 得到  target 的最少操作次数，每次操作需遵循以下规则：

    在 initial 中选择 任意 子数组，并将子数组中每个元素增加 1 。

答案保证在 32 位有符号整数以内。



示例 1：

输入：target = [1,2,3,2,1]
输出：3
解释：我们需要至少 3 次操作从 intial 数组得到 target 数组。
[0,0,0,0,0] 将下标为 0 到 4 的元素（包含二者）加 1 。
[1,1,1,1,1] 将下标为 1 到 3 的元素（包含二者）加 1 。
[1,2,2,2,1] 将下表为 2 的元素增加 1 。
[1,2,3,2,1] 得到了目标数组。

示例 2：

输入：target = [3,1,1,2]
输出：4
解释：(initial)[0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2] (target) 。

示例 3：

输入：target = [3,1,5,4,2]
输出：7
解释：(initial)[0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1]
                                  -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2] (target)。

示例 4：

输入：target = [1,1,1,1]
输出：1



提示：

    1 <= target.length <= 10^5
    1 <= target[i] <= 10^5
"""
from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        stack = []
        res = 0
        for num in target:
            if len(stack) == 0:
                res += num
                stack.append(num)
            elif stack[-1] <= num:
                res += num - stack[-1]
                stack.append(num)
            else:
                while len(stack) > 0 and stack[-1] > num:
                    stack.pop()
                stack.append(num)
        return res


if __name__ == '__main__':
    print(Solution().minNumberOperations([1, 2, 3, 2, 1]), 3)
    print(Solution().minNumberOperations([3, 1, 1, 2]), 4)
    print(Solution().minNumberOperations([3, 1, 5, 4, 2]), 7)
    print(Solution().minNumberOperations([1, 1, 1, 1]), 1)
    print(Solution().minNumberOperations([1, 2, 3, 1, 2, 3, 2, 1, 3]), 7)
