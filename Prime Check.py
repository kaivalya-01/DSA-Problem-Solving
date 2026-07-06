Given a number n, determine whether it is a prime number or not.
Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False

        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1

        return True
        
