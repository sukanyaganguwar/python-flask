def repeat(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat(7)
def say_hello():
    print("Hellloooo....")

say_hello()    