def slow_fun():
    print("running slowly .......")
    print("running slowly .......")
    print("running slowly .......")
    print("running slowly .......")
    print("running slowly .......")
    return 10

if(a:= slow_fun() > 9):
    print(a)
else:
    print("Its not a greater number")



# Example2

# while(data:= input("Enter the value:")):
#     print(data)
#     if data == "q":
#         break


# for example2 if you just press blank value, it will stop , because blank means false. if you enter value then "while" condition will be true