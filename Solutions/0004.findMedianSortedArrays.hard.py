"""
# 4. 寻找两个有序数组的中位数

## 题意

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

**示例1:**
```
输入: nums1 = [1, 3], nums2 = [2]
输出: 2.0
```
**示例2:**
```
输入: nums1 = [1, 2], nums2 = [3, 4]
输出: 2.5
原因: (2 + 3)/2 = 2.5
```

## 题解
求中位数可以稍微转化一下，求第k大（小）。
因为都是有序数组，可以发现，一个数组最长为k，因为大于k的部分一定不是解，可以舍弃。
进一步可以发现，两数组长度不是k和k-1就是两个都是k。
因为当两数组长度之和L小于2*k-1时，求第k大（小）可以转化为求第L-k+1小（大）。

以第k大为例。先根据上述情况对数组长度和k进行处理。
每次取`a=nums1[k//2]`,`b=nums2[k-k//2]`，大约都位于两数组的中间且位数和为k。
比较a、b大小，若a<b，b至少是第k大数，则`nums2`中b之后的都可以舍去，这些数较所求大，
a最多只有第k-1大，则`nums1`中a之前包括a也可以舍去，这些数较所求小。
问题转化为子问题求`nums1[k//2+1:]`和`nums2[:k-k//2]`中第`k-k//2`大的数。
每次问题规模缩小一半，时间复杂度O(log(n+m))。
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 == 0 and l2 == 0:
            return 0
        elif (l1 + l2) % 2 == 1:
            return self.fingKSortedArrays(nums1, nums2, (l1 + l2 + 1) // 2)
        else:
            a = self.fingKSortedArrays(nums1, nums2, (l1 + l2) // 2)
            b = self.fingKSortedArrays(nums1, nums2, (l1 + l2) // 2 + 1)
            return (a + b) / 2

    def fingKSortedArrays(self, nums1: List[int], nums2: List[int], k: int) -> int:
        i, j = 0, 0
        while k:
            if i == len(nums1):
                return nums2[j + k - 1]
            elif j == len(nums2):
                return nums1[i + k - 1]
            elif k == 1:
                return nums1[i] if nums1[i] < nums2[j] else nums2[j]
            l1 = min(k // 2, len(nums1) - i)
            l2 = min(k - l1, len(nums2) - j)
            if nums1[i + l1 - 1] <= nums2[j + l2 - 1]:
                i += l1
                k -= l1
            else:
                j += l2
                k -= l2
        return 0


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 3], [2]), 2,)
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]), 2.5)
