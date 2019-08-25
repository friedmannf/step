# noinspection SpellCheckingInspection
__author__ = "Felix Friedmann"
__copyright__ = "Copyright 2019"

from step import step


@step
def test_func(n: int):
    """ A function consuming some time to demonstrate the timing functionality """
    o = 0
    for i in range(n):
        o *= i
        o -= i
    return


if __name__ == '__main__':
    """ Run this and observe that timing info will be logged """
    test_func(500)
    test_func(5000)
    test_func(10000)
