from typing import Callable, Iterator

# iterative
def fib_iter() -> Iterator[int]:
    """ Generates an infinite sequence of Fibonacci """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# recursive
def fib_rec(n: int) -> int:
    """ Returns Fibonacci number at n position """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)


def sequence_iter(n: int) -> List[int]:
    pass


def sequence_rec(n: int) -> List[int]:
    pass


def sum_fibs(n: int, m: int, f: Callable) -> int:
    pass
