class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        s = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        index = 0
        while num > 0:
            x = num % 10
            if x < 5:
                if x == 4:
                    temp = s[index] + s[index + 1]
                else:
                    temp = ""
                    while x > 0:
                        temp += s[index]
                        x -= 1
            else:
                if x == 9:
                    temp = s[index] + s[index + 2]
                else:
                    temp = s[index + 1]
                    while x > 5:
                        temp += s[index]
                        x -= 1
            index += 2
            res = temp + res
            num = num // 10
        return res


if __name__ == '__main__':
    print(
        Solution().intToRoman(3), "III",
        Solution().intToRoman(4), "IV",
        Solution().intToRoman(9), "IX",
        Solution().intToRoman(58), "LVIII",
        Solution().intToRoman(1994), "MCMXCIV",
    )
