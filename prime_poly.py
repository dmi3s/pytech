from math import isqrt
from typing import Iterable, Callable
from functools import wraps
from time import time
from primePy import primes
import sympy


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' %
              (f.__name__, args, kw, te - ts))
        return result

    return wrap


def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False


_FIRST_PRIME_RUN = ('1', '3', '5', '7', '9')
_FIRST_RUN = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
_ALL_RUN = ('0',) + _FIRST_RUN


def gen_all(prev: str, w: int, run: tuple[str, ...] = _FIRST_RUN) -> Iterable[str]:
    if w == 0:
        yield prev
    else:
        for digit in run:
            for nxt in gen_all(prev + digit, w - 1, _ALL_RUN):
                yield nxt


def gen(n: int, first_run: tuple[str, ...] = _FIRST_RUN) -> Iterable[int]:
    w_left, w_center = divmod(n, 2)
    for c in gen_all("", w_center, _ALL_RUN):
        for left in gen_all("", w_left, first_run):
            yield int(left + c + left[::-1])


def gen_prime(n: int, prime_test: Callable[[int], bool]) -> Iterable[int]:
    return (p for p in gen(n, _FIRST_PRIME_RUN) if prime_test(p))


__N = 11


@timing
def test_is_prime():
    cnt = 0
    for v in gen_prime(__N, is_prime):
        # print(v)
        cnt += 1
    print(f"Total: {cnt}")


@timing
def test_prime_py():
    cnt = 0
    for v in gen_prime(__N, primes.check):
        # print(v)
        cnt += 1
    print(f"Total: {cnt}")


@timing
def test_sym_py():
    cnt = 0
    for v in gen_prime(__N, sympy.isprime):
        # print(v)
        cnt += 1
    print(f"Total: {cnt}")


def main():
    print(f"__N = {__N}")
    test_is_prime()
    test_prime_py()
    test_sym_py()


# __N = 11
# Total: 42042
# func:'test_is_prime' args:[(), {}] took: 69.8690 sec
# Total: 42042
# func:'test_prime_py' args:[(), {}] took: 112.9230 sec
# Total: 42042
# func:'test_sym_py' args:[(), {}] took: 1.2725 sec
# WTF?!!111                              ^^^^^^


if __name__ == '__main__':
    main()
