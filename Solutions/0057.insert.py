# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/27 15:48
"""
57. 插入区间

给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]

示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        l = 0
        r = len(intervals) - 1
        index = len(intervals)
        while l <= r:
            m = (l+r)//2
            if intervals[m][0] < newInterval[0]:
                l = m+1
            else:
                index = m
                r = m-1
        if index > 0 and intervals[index-1][1] >= newInterval[0]:
            index -= 1
            newInterval[0] = intervals[index][0]
            newInterval[1] = max(intervals[index][1], newInterval[1])
            intervals.pop(index)
        while index < len(intervals) and intervals[index][0] <= newInterval[1]:
            newInterval[1] = max(intervals[index][1], newInterval[1])
            intervals.pop(index)
        intervals.insert(index, newInterval)
        return intervals


if __name__ == '__main__':
    print(
        Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]),
        Solution().insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]),
    )

