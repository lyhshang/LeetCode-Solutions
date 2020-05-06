class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 因为负数边界比正数边界大，因此转负数计算较为方便
        sign = (dividend > 0) ^ (divisor > 0)
        if dividend > 0:
            dividend = -dividend
        if divisor > 0:
            divisor = -divisor
        res = 0
        jishu = -1
        while divisor >= ~0x3FFFFFFF and dividend <= (divisor << 1):
            divisor <<= 1
            jishu <<= 1
        while jishu != 0:
            if dividend <= divisor:
                dividend -= divisor
                res += jishu
            jishu = jishu >> 1 if jishu < -1 else 0
            divisor >>= 1
        if not sign:
            if res == ~0x7FFFFFFF:
                return 0x7FFFFFFF
            res = -res
        return res


if __name__ == '__main__':
    print(
        Solution().divide(10, 3), 3,
        Solution().divide(7, -3), -2,
    )
