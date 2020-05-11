# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/11 9:44
"""
fastPower
快速幂
log(n)时间求x^n,n需要为整数
"""


def fast_power(x: float, n: int) -> float:
    if n < 0:
        x = 1. / x if x != 0 else 0
        n = -n
    res = 1
    while n:
        if n & 1 == 1:
            res *= x
        x *= x
        n //= 2
    return res
