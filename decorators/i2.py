
def my_decorator(func):

    def wrap_fun(*arg, **kwargs):
        print("*****wrap_fun*****")
        func(*arg, **kwargs)
        print("*****wrap_fun_2*****")

    return wrap_fun


@my_decorator
def say_hello(*arg):
    print(f"Hello {arg}")


say_hello("Test", "Second", "Third")
