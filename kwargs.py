def marks(**kwargs):
    print(kwargs)
    for item in kwargs.keys():
        print(f" The marks of {item} is {kwargs[item]}")

marks(jenny = 10, markos = 30, alena = 20)        