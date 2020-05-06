"""
# 7. 整数反转

## 题意
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

**示例1:**
```
输入: 123
输出: 321
```
**示例2:**
```
输入: -123
输出: -321
```
**示例3:**
```
输入: 120
输出: 21
```
**注意:**

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2<sup>31</sup>,  2<sup>31</sup> − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

## 题解
简单的数学问题，初始化`res`为0,
每次将`res`左移一位(乘10),将输入`x`右移一位(除10)
将`x`移出的数字加到`res`上，直到`x`为0。

注意数据范围是32位，结果溢出的输出0，在`res`每次更新增大前判断是否会溢出。

注意正负号,因为正、负上限的反转都是溢出的，
所以可以统一转化为正数计算，不必考虑正、负的边界差异。
"""

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        up = 2147483647
        flag = False
        if x < 0:
            x = -x
            flag = True
        while x:
            if res > up // 10 or res * 10 > up - x % 10:
                return 0
            res = res * 10 + x % 10
            x //= 10
        res = -res if flag else res
        return res


if __name__ == '__main__':
    print(
        Solution().reverse(123),
        Solution().reverse(-123),
        Solution().reverse(120),
    )
