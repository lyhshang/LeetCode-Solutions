# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/5 11:00
"""
5455. 最多 K 次交换相邻数位后得到的最小整数

给你一个字符串 num 和一个整数 k 。其中，num 表示一个很大的整数，字符串中的每个字符依次对应整数上的各个 数位 。

你可以交换这个整数相邻数位的数字 最多 k 次。

请你返回你能得到的最小整数，并以字符串形式返回。



示例 1：

输入：num = "4321", k = 4
输出："1342"
解释：4321 通过 4 次交换相邻数位得到最小整数的步骤如上图所示。

示例 2：

输入：num = "100", k = 1
输出："010"
解释：输出可以包含前导 0 ，但输入保证不会有前导 0 。

示例 3：

输入：num = "36789", k = 1000
输出："36789"
解释：不需要做任何交换。

示例 4：

输入：num = "22", k = 22
输出："22"

示例 5：

输入：num = "9438957234785635408", k = 23
输出："0345989723478563548"



提示：

    1 <= num.length <= 30000
    num 只包含 数字 且不含有 前导 0 。
    1 <= k <= 10^9
"""
from typing import List


class mystr:
    def __init__(self, num: str):
        self.slist = list(num)
        self.q = []  # 交换操作序列

    def getstring(self) -> list:
        res = []
        index = 0   # slist的下标
        j = 0   # q下标，用i == self.q[j][0]时替换
        k = 0   # q下标，跳过index == self.q[k][1]
        for i in range(len(self.slist)):
            if j < len(self.q) and i == self.q[j][0]:
                res.append(self.slist[self.q[j][1]])
                j += 1
            else:
                while k < len(self.q) and index == self.q[k][1]:
                    index += 1
                    k += 1
                res.append(self.slist[index])
                index += 1
        for i in range(len(self.slist)):
            self.slist[i] = res[i]
        self.q.clear()
        return res

    def front(self, l: int, r: int):
        self.q.append((l, r))


class Solution:
    # 判断a比b小
    def low(self, a: List, b: List) -> bool:
        k = 0
        for i in range(len(a)):
            if int(a[i]) != int(b[i]):
                k = i
                break
        if k < len(a) and int(a[k]) < int(b[k]):
            return True
        return False

    def minInteger(self, num: str, k: int) -> str:
        s = mystr(num)

        le = 0  # 左端点
        spare = ['9' for i in range(len(num))]
        for i in range(10):
            clist = s.getstring()
            args = [
                index for index in range(
                    len(clist)) if int(
                    clist[index]) == i]

            for j in args:
                if j - le <= k:
                    s.front(le, j)

                    k -= j - le
                    le += 1
                else:
                    temp = s.getstring()
                    z = temp[j]
                    temp.pop(j)
                    temp.insert(j - k, z)

                    if self.low(temp, spare):
                        spare = temp
                    break

        clist = s.getstring()
        if self.low(spare, clist):
            clist = spare

        res = ''.join(clist)
        return res


if __name__ == '__main__':
    print(
        # Solution().minInteger("36789", 1000), "36789",
        Solution().minInteger("294984148179", 11), "124498948179"
    )
