from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = -1
        best_delta = 1e9 + 7
        for k in range(len(nums) - 2):
            if nums[k] * 3 - target > best_delta:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i = k + 1
            j = len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if abs(s - target) < best_delta:
                    res = s
                    best_delta = abs(s - target)
                if s - target > 0:
                    j -= 1
                elif s - target < 0:
                    i += 1
                else:
                    return s
        return res


if __name__ == '__main__':
    print(
        Solution().threeSumClosest([1, 1, 1, 1], 0), 2,
    )
