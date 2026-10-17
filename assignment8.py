# # decotor fun

# def logger(func):
#     def wrapper():
#             print("running slowly .......")
#             func()
#     return wrapper

# @logger
# def say_hello():
#     print("Hellllooooo....")


# say_hello()



# Example 2

import time


def timer(func):
    def wrapper():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f}")
    return wrapper


@timer
def sum():
    total = 0
    for i in range(1,1000001):
        total += i

    return total   


sum()