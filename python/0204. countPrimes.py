# sieve of Eratosthenes
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        sieve = [1] * n
        sieve[0] = sieve[1] = 0

        root = int(n ** 0.5)
        for i in range(2, root+1):
            if not sieve[i]:
                continue
            sieve[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)

        return sum(sieve)
