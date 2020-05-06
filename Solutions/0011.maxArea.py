from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            res = max(res, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res


if __name__ == '__main__':
    print(
        Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49,
    )
