class Solution:
    def is_32bit(self, n: int) -> bool:
         return True if -2**31 <= n <= 2**31 - 1 else False

    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        return 0 if self.is_32bit(rev) == False else -1*rev if x < 0 else rev
