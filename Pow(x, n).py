Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1.0

        if n < 0:
            x = 1 / x
            n = -n

        ans = 1.0

        while n > 0:
            if n % 2 == 1:
                ans *= x
            x *= x
            n //= 2

        return ans
        
