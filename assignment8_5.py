from functools import reduce


num = [1, 2, 3, 4, 5]

print(list(map(lambda x: x*x*x , num)))


num = [10, 11, 12, 13, 14]

print(list(filter(lambda x: (x%2==0),num)))


p = [1, 2, 3, 4]

def prod(a,b):
    return a*b

prod = reduce(prod, p)

print(prod)


