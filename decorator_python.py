def decorator(func):
    def wrapper():
        print("Function is started...")
        func()
        print("Function is executed...")
    return wrapper

@decorator
def say_hello():
    print("Hi, Good Morning!")

say_hello()    
