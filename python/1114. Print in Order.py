from threading import Lock, Event

# events
class Foo:
    def __init__(self):
        self.event1 = Event()
        self.event2 = Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.event1.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.event1.wait()
        printSecond()
        self.event2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.event2.wait()
        printThird()

# locks
class Foo:
    def __init__(self):
        self.lock1 = Lock()
        self.lock1.acquire()
        self.lock2 = Lock()
        self.lock2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.lock1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.lock1.acquire()
        printSecond()
        self.lock2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.lock2.acquire()
        printThird()

# sleep
class Foo:
    def __init__(self):
        self.state = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.state += 1

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.state != 1:
            time.sleep(0.001)
        printSecond()
        self.state += 1

    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.state != 2:
            time.sleep(0.001)
        printThird()
