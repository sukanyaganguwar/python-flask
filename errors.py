while True:
    try:
        a = int(input("Enter the number first: "))
        b = int(input("Enter the number second: "))

        print(f" The sum of this number is : {a/b}")

    except ValueError:
        print("Dont pass wrong values")

    except ZeroDivisionError:
        print("zeros are getting") 

    except Exception as e:
        print(f"Exception raised", e.args)  
