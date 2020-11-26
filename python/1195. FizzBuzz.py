from threading import Lock

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.number_lock = Lock()

        self.fizzbuzz_lock = Lock()
        self.fizzbuzz_lock.acquire()

        self.fizz_lock = Lock()
        self.fizz_lock.acquire()

        self.buzz_lock = Lock()
        self.buzz_lock.acquire()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for x in range(1, self.n+1):
            self.number_lock.acquire()
            if x % 15 == 0:
                self.fizzbuzz_lock.release()
            elif x % 3 == 0:
                self.fizz_lock.release()
            elif x % 5 == 0:
                self.buzz_lock.release()
            else:
                printNumber(x)
                self.number_lock.release()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for x in range(self.n//15):
            self.fizzbuzz_lock.acquire()
            printFizzBuzz()
            self.number_lock.release()

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for x in range(self.n//3 - self.n//15):
            self.fizz_lock.acquire()
            printFizz()
            self.number_lock.release()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for x in range(self.n//5 - self.n//15):
            self.buzz_lock.acquire()
            printBuzz()
            self.number_lock.release()
