a = [12,45,16,1,2, 5, 9,21]

def check_num(a):
    if a > 9:
        return True
    else: 
        return False

new = list(filter(check_num, a))
# also other way to do this using lambda function and get rid of func check_num
new1 = list(filter(lambda x: x>9, a))

print(new)

print(new1)