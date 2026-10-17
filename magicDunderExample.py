class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return ((self.x + other.x), (self.y + other.y))    

    def __mul__(self, other):
        return (self.x * other.x, self.y * other.y)


v1 = Vector(8,2)
v2 = Vector(6,3)

v3 = v1 + v2

v4 = v1 * v2

print(v3)
print(v4)