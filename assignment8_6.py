# example 1 walrus operator
while (data := input("Enter the number(press'quit' to exist)")) != "quit":
      print(data)

# example 2
words =["python", "rocks", "ar"]

lengths = [length for word in words if (length := len(word)) >=4]

print(lengths)