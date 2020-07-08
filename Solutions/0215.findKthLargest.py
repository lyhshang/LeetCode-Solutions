# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/8 19:08
"""
215. 数组中的第K个最大元素

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def down(index):
            while index*2+1 < k:
                target = index
                l = index*2+1
                r = l + 1
                if nums[l] < nums[target]:
                    target = l
                if r < k and nums[r] < nums[target]:
                    target = r
                if target != index:
                    nums[index], nums[target] = nums[target], nums[index]
                    index = target
                else:
                    break
        for i in range(k//2, -1, -1):
            down(i)
        for i in range(k, len(nums)):
            if nums[i] > nums[0]:
                nums[0] = nums[i]
                down(0)
        return nums[0]


if __name__ == '__main__':
    # assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
