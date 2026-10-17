# num = [ 10,20,10,30, 40, 50, 40, 20]

# con_set = set(num)

# print(con_set)


products = [
    { "name" : "TV", "price" : "580000"},
    { "name" : "Mobile", "price" : "180000"},
    { "name" : "Oven", "price" : "980000"}
]

temp = 0

for i in products:
    price = i["price"]
    if int(temp) < int(price):
       temp = price

print(temp)       
