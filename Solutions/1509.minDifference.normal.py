# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/11 22:28
"""
1509. 三次操作后最大值与最小值的最小差

给你一个数组 nums ，每次操作你可以选择 nums 中的任意一个元素并将它改成任意值。

请你返回三次操作后， nums 中最大值与最小值的差的最小值。



示例 1：

输入：nums = [5,3,2,4]
输出：0
解释：将数组 [5,3,2,4] 变成 [2,2,2,2].
最大值与最小值的差为 2-2 = 0 。

示例 2：

输入：nums = [1,5,0,10,14]
输出：1
解释：将数组 [1,5,0,10,14] 变成 [1,1,0,1,1] 。
最大值与最小值的差为 1-0 = 1 。

示例 3：

输入：nums = [6,6,0,1,1,4,6]
输出：2

示例 4：

输入：nums = [1,5,6,14,15]
输出：1



提示：

    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def __rck(self, k, nums):
        if k == 3:
            self.res = min(self.res, nums[-1] - nums[0])
        else:
            a = nums[0]
            nums.pop(0)
            self.__rck(k + 1, nums)
            nums.insert(0, a)

            a = nums[-1]
            nums.pop()
            self.__rck(k + 1, nums)
            nums.append(a)

    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4:
            return 0
        else:
            index = []
            for i in range(4):
                if i not in index:
                    index.append(i)
                if len(nums) - i - 1 not in index:
                    index.append(len(nums) - i - 1)
            temp_nums = sorted([nums[i] for i in index])
            self.res = temp_nums[-1] - temp_nums[0]
            self.__rck(0, temp_nums)
            return self.res


if __name__ == '__main__':
    print(
        Solution().minDifference(nums=[5, 3, 2, 4]), 0,
        Solution().minDifference(nums=[1, 5, 0, 10, 14]), 1,
        Solution().minDifference(nums=[6, 6, 0, 1, 1, 4, 6]), 2,
    )
