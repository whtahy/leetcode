from threading import Lock

class DiningPhilosophers:
    def __init__(self):
        self.forks = [Lock()] * 5

    def wantsToEat(
        self,
        philosopher: int,
        pickLeftFork: 'Callable[[], None]',
        pickRightFork: 'Callable[[], None]',
        eat: 'Callable[[], None]',
        putLeftFork: 'Callable[[], None]',
        putRightFork: 'Callable[[], None]'
    ) -> None:

        left = philosopher
        right = (philosopher-1) % 5
        with self.forks[left] and self.forks[right]:
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()
