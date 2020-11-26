from threading import Barrier, Lock

# barrier
class FooBar:
    def __init__(self, n):
        self.n = n
        self.barrier = Barrier(2)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            printFoo()
            self.barrier.wait()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.barrier.wait()
            printBar()

# locks
class FooBar:
    def __init__(self, n):
        self.n = n
        self.l_foo = Lock()
        self.l_bar = Lock()
        self.l_bar.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.l_foo.acquire()
            printFoo()
            self.l_bar.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.l_bar.acquire()
            printBar()
            self.l_foo.release()

# sleep
class FooBar:
    def __init__(self, n):
        self.n_foo = n
        self.n_bar = n

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        while self.n_foo > 0:
            if self.n_foo == self.n_bar:
                printFoo()
                self.n_foo -= 1
            else:
                time.sleep(0.001)

    def bar(self, printBar: 'Callable[[], None]') -> None:
        while self.n_bar > 0:
            if self.n_bar > self.n_foo:
                printBar()
                self.n_bar -= 1
            else:
                time.sleep(0.001)
