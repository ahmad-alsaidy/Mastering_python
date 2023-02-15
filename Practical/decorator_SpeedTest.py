# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------

from time import time


def speed_test(func):
    def wrapper():
        start = time()
        func()
        end = time()

        print(f"Function Running Time Is: {end - start}")
    return wrapper


@speed_test
def bigLoop():
    for i in range(20000):
        print(i)


bigLoop()
