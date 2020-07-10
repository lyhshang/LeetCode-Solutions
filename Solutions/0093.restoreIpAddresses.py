# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/10 23:46
"""
93. 复原IP地址

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。



示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        temp = ['0' for i in range(4)]
        res = []

        def rcs(k: int, index: int):
            if k == 3:
                temp[k] = s[index:]
                if temp[k][0] == '0' and len(temp[k]) > 1:
                    return
                if int(temp[k]) >= 256:
                    return
                z = ''
                for i in range(4):
                    z += temp[i] if i == 0 else '.' + temp[i]
                res.append(z)
            else:
                for i in range(1, 4):
                    if index + i >= len(s):
                        break
                    temp[k] = s[index:index + i]
                    if temp[k][0] == '0' and i > 1:
                        break
                    if int(temp[k]) >= 256:
                        break
                    rcs(k + 1, index + i)
        rcs(0, 0)
        return res


if __name__ == '__main__':
    print(
        Solution().restoreIpAddresses("25525511135"),
        Solution().restoreIpAddresses("0000"),
        Solution().restoreIpAddresses("010010"),
    )
