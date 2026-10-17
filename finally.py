def division(a,b):
    try: 
        c = a/b
        print(c)
        return c
    except Exception as e:
        print(e)
        return None
    finally:
        print("This should always be executed")  #If we want some function to do some cleanup process 
                                                 # we can add it in finally



a = int(input("Enter the number first:"))
b = int(input("Enter the number second:"))

division(a,b)