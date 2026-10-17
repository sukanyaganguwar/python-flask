class MyException(Exception):
    pass

try:
    a = int(input("Enter the number :"))
    if a < 0:
        raise MyException("The number cannot be negative")
    print(a)
except ValueError:
    print("Its not a number, please enter some number not character")    
except ZeroDivisionError:
    print("zero")
except MyException as e:
    print(e)    

    