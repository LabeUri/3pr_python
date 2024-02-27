class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def subtract(self, other):
        return Vector(self.x - other.x, self.y - other.y)

v1 = Vector(8, 4)
v2 = Vector(1, 12)

result_add = v1.add(v2)
print("Додавання векторів:", result_add.x, result_add.y)

result_subtract = v1.subtract(v2)
print("Віднімання векторів:", result_subtract.x, result_subtract.y)
