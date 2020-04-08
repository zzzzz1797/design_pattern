"""
    装饰器模式：以透明的方式(不会影响其他对象)动态地将功能添加到一个对象中。
    使用装饰器进行一层额外的封装，基于某个条件来决定是否执行真正的装饰器。

"""
from functools import wraps


def cache(size=None):
    def _(func):
        memo = {}

        @wraps(func)
        def __(*args):
            if args not in memo:
                memo[args] = func(*args)
            return memo[args]

        return __

    if callable(size):
        return _(size)
    else:
        return _


def fib1(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1

    return fib1(n - 1) + fib1(n - 2)


@cache
def fib2(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1

    return fib2(n - 1) + fib2(n - 2)


if __name__ == '__main__':
    # print(fib1(10))

    # cache 代表 cache(fib2(100))
    # print(fib2(100))
    func1 = cache(fib2)
    print(func1(100))

    func2 = cache(100)(fib2)
    print(func2(100))
