from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums) - 3):
            if k == 0 or nums[k] != nums[k - 1]:
                if nums[k] * 4 > target:
                    break
                for h in range(k + 1, len(nums) - 2):
                    if h == k + 1 or nums[h] != nums[h - 1]:
                        if nums[k] + nums[h] * 3 > target:
                            break
                        i = h + 1
                        j = len(nums) - 1
                        while i < j:
                            s = nums[k] + nums[h] + nums[i] + nums[j]
                            if s > target:
                                while i < j and nums[j - 1] == nums[j]:
                                    j -= 1
                                j -= 1
                            elif s < target:
                                while i < j and nums[i + 1] == nums[i]:
                                    i += 1
                                i += 1
                            else:
                                res.append(
                                    [nums[k], nums[h], nums[i], nums[j]])
                                while i < j and nums[j - 1] == nums[j]:
                                    j -= 1
                                while i < j and nums[i + 1] == nums[i]:
                                    i += 1
                                j -= 1
                                i += 1
        return res


if __name__ == '__main__':
    print(
        Solution().fourSum([1, 0, -1, 0, -2, 2], 0), [
            [-1, 0, 0, 1],
            [-2, -1, 1, 2],
            [-2, 0, 0, 2]
        ],
    )
