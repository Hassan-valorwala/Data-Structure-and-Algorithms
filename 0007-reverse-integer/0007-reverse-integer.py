class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        rev = 0
        while (x > 0) :
            l = x%10
            rev = rev*10+l
            x = x//10

        rev *= sign

        if rev > 2**31 or rev < -2**31:
            return 0
        else:
            return rev           


        