# set
class Solution:
    def isHappy(self, n: int) -> bool:
        def f(x):
            return sum(int(x)**2 for x in str(x))

        history = set()
        while n != 1:
            history.add(n)
            n = f(n)
            if n in history:
                return False
        return True

# Floyd's cycle algorithm
class Solution:
    def isHappy(self, n: int) -> bool:
        def f(x):
            return sum(int(x)**2 for x in str(x))

        slow, fast = n, f(n)
        while True:
            if slow == 1 or fast == 1:
                return True
            elif slow == fast:
                return False
            slow = f(slow)
            fast = f(f(fast))
