x = [1,2,3,4,5]

def square(x):
    return x * x

# new = list(map(square,x))

# either way to do it is using lambda function

new=list(map(lambda x: x * x, x))

print(new)