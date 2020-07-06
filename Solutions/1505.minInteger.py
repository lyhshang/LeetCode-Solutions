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
"""
代码源自leecode@pastfoever
"""
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        info = [[] for _ in range(10)]
        cur_pos = [0] * 10  # info中每个数字下一个可前移的位置的索引
        cur_offset = [0] * 10  # 0-9每个数字的下一个可前移位置的偏移
        history = [0] * len(num)  # num中对应的数字是否前移，前移(-1)，未前移(0)
        res = []
        # 记录下所有数字在num中的位置
        for i, v in enumerate(num):
            info[int(v)].append(i)

        while k and len(res) < len(num):
            # 从0开始找可以前移的数字
            for i in range(10):
                if cur_pos[i] < len(info[i]) and info[i][cur_pos[i]] + \
                        cur_offset[i] <= len(res) + k:  # 符合前移条件
                    k -= info[i][cur_pos[i]] + \
                        cur_offset[i] - len(res)  # k减去消耗的前移步数
                    res.append(str(i))
                    history[info[i][cur_pos[i]]] -= 1  # 标记前移的数字

                    # 0-9每个数字更新由于本次前移造成的偏移
                    for j in range(10):
                        if cur_pos[j] < len(
                                info[j]) and info[i][cur_pos[i]] >= info[j][cur_pos[j]]:
                            cur_offset[j] += 1

                    cur_pos[i] += 1  # 当前数字的下一个可前移位置的索引
                    # 更新当前数字的偏移(每遇到一个已经前移的数字，偏移减1)
                    if cur_pos[i] < len(info[i]):
                        for j in range(info[i][cur_pos[i] - 1],
                                       info[i][cur_pos[i]]):
                            cur_offset[i] += history[j]

                    break
        # 添加所有未前移的数字
        for i in range(len(num)):
            if history[i] == 0:
                res.append(num[i])
        return ''.join(res)


if __name__ == '__main__':
    print(
        Solution().minInteger("3132", 2), "1323",
        Solution().minInteger("36789", 1000), "36789",
        Solution().minInteger("294984148179", 11), "124498948179"
    )
