# closed form
class Solution:
    def fib(self, N: int) -> int:
        a = (1 + sqrt(5)) / 2
        b = (1 - sqrt(5)) / 2
        return round((a ** N - b ** N) / sqrt(5))

# iterative
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, N+1):
            c = a + b
            a, b = b, c
        return c

# recursive
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        return Solution.fib(self, N-2) + Solution.fib(self, N-1)
