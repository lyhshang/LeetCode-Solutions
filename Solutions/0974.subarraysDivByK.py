# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/27 20:50
"""
974. 和可被 K 整除的子数组

给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。



示例：

输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]



提示：

    1 <= A.length <= 30000
    -10000 <= A[i] <= 10000
    2 <= K <= 10000
"""
from typing import List


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        sum = 0
        nums = {0: 1}
        res = 0
        for a in A:
            sum += a
            k = sum % K
            num = nums.get(k, 0)
            res += num
            nums[k] = num + 1
        return res


if __name__ == '__main__':
    print(
        Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5), 7,
    )
