# decorator is a type of function that inputs a function and return a modified version of the function


def announce(f):  # defining a decorator
    def wrapper():
        print("about to run a function")
        f()
        print("Done with the function")
    return wrapper


@announce  # called a function as a decorator
def Hello():
    print("Hello, Word")


Hello()
