"""
Przeciążanie operatorów
"""


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def add_vector(v1, v2):
        return Vector(v1.x + v2.x, v1.y + v2.y)

    def __str__(self):
        return f"X: {self.x} Y: {self.y}"

    def __add__(self, other):
        if type(other) in [int, float]:
            return Vector(self.x + other, self.y + other)
        return Vector(self.x + other.x, self.y + other.y)


vector1 = Vector(3, 2)
vector2 = Vector(2, 2)
vector3 = Vector.add_vector(vector1, vector2)
vector4 = vector1 + vector2
vector5 = vector1 + 2

print(vector1, vector2, "|", vector3, "|", vector4, "|", vector5)
