"""
# 1. 两数之和

## 题意
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

**示例1:**
```
输入: nums = [2, 7, 11, 15], target = 9
输出: [0, 1]
原因: nums[0] + nums[1] = 2 + 7 = 9
```

## 题解
扫描一遍，记录各个数的下标，对当前数`cur`查询`target-cur`的下标，若存在即所求。
"""


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            require = target-nums[i]
            if m.get(require) is not None:
                return [m.get(require), i]
            else:
                m[nums[i]] = i


if __name__ == '__main__':
    print(
        Solution().twoSum([2, 7, 11, 15], 9)
    )
