class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        back = 0
        y = x
        while y:
            back *= 10
            back += y % 10
            y //= 10
        return back == x


if __name__ == '__main__':
    print(
        Solution().isPalindrome(121), True,
        Solution().isPalindrome(-121), False,
        Solution().isPalindrome(10), False,
    )
