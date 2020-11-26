from threading import Barrier, Semaphore

class H2O:
    def __init__(self):
        self.barrier = Barrier(3)
        self.h_queue = Semaphore(2)
        self.o_queue = Semaphore(1)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.h_queue:
            self.barrier.wait()
            releaseHydrogen()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.o_queue:
            self.barrier.wait()
            releaseOxygen()
