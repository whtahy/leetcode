from threading import Lock

# locks
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.l_zero = Lock()
        self.l_even = Lock()
        self.l_even.acquire()
        self.l_odd = Lock()
        self.l_odd.acquire()

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for x in range(1, self.n+1):
            self.l_zero.acquire()
            printNumber(0)
            if x % 2 == 0:
                self.l_even.release()
            else:
                self.l_odd.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for x in range(1, self.n+1, 2):
            self.l_odd.acquire()
            printNumber(x)
            self.l_zero.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for x in range(2, self.n+1, 2):
            self.l_even.acquire()
            printNumber(x)
            self.l_zero.release()

# sleep
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.i = 1
        self.zed = True

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while self.i <= self.n:
            if self.zed:
                printNumber(0)
                self.zed = False
            else:
                time.sleep(0.001)

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while self.i <= self.n:
            if not self.zed and self.i % 2 == 1:
                printNumber(self.i)
                self.i += 1
                self.zed = True
            else:
                time.sleep(0.001)

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while self.i <= self.n:
            if not self.zed and self.i % 2 == 0:
                printNumber(self.i)
                self.i += 1
                self.zed = True
            else:
                time.sleep(0.001)
