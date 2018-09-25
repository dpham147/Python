class Vector:
    def __init__(self, x, y, z):
        self.__x, self.__y, self.__z = x, y, z

    # Create is a class method invoked by the class and does not take self as a param
    @classmethod
    def create(cls, pointa, pointb):
        return cls(pointb.x - pointa.x,
                   pointb.y - pointa.y,
                   pointb.z - pointa.z)

    # Alternatively implementation as a static method
    @staticmethod
    def create(pointa, pointb):
        return Vector(pointb.x - pointa.x,
                      pointb.y - pointa.y,
                      pointb.z - pointa.z)

    def getx(self): return self.__x
    def gety(self): return self.__y
    def getz(self): return self.__z

    # How to set a private variable
    def setx(self, x): self.__x = x
    def sety(self, y): self.__y = y
    def setz(self, z): self.__z = z

    x = property(getx, setx)
    y = property(gety, sety)
    z = property(getz, setz)

    # Allow vector addition
    def __add__(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y,
                      self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x,
                      self.y - other.y,
                      self.z - other.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(self.y * other.z - self.z - other.y,
                      self.z * other.x - self.x - other.z,
                      self.x * other.y - self.y - other.x)

    def __str__(self): return 'Vector(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'


a = Vector(0, 0, 0)
b = Vector(1, 1, 1)

print(str(a))
print(str(b))
print(str(b + b))
print(str(-b))

