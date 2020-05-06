from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        if len(nums) < 3:
            return res
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i = k + 1
            j = len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s > 0:
                    while i < j and nums[j - 1] == nums[j]:
                        j -= 1
                    j -= 1
                elif s < 0:
                    while i < j and nums[i + 1] == nums[i]:
                        i += 1
                    i += 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    while i < j and nums[j - 1] == nums[j]:
                        j -= 1
                    while i < j and nums[i + 1] == nums[i]:
                        i += 1
                    j -= 1
                    i += 1
        return res


if __name__ == '__main__':
    print(
        Solution().threeSum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]],
    )
