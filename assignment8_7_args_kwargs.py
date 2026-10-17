def print_details(**kwargs):
    print(kwargs)

print_details(name="Alice", age=25, city="Delhi")


def sum_all(*awrgs):
    total =0
    for item in awrgs:
        total += item
    return total

print(sum_all(10,20,40))    
