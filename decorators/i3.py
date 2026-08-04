
from time import time


def performance(fun):
    def wrap_fun(*arg, **kwargs):
        start_micro = time()
        result = fun(*arg, **kwargs)
        end_micro = time()

        print(
            f"Function finished executing in {end_micro - start_micro} seconds")

        return result
    return wrap_fun


@performance
def heavy_operation():
    for item in range(300000000):
        item*5
    return "finished"


res = heavy_operation()
print(res)
