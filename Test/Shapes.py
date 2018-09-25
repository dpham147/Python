import math


class Point:
    def __init__(self, x, y): self.__x, self.__y = x, y

    def __str__(self): return 'Point(' + str(self.__x) + ',' + str(self.__y) + ')'

    def __le__(self, other): return self.__x <= other.__x and self.__y <= other.__y

    def x(self): return self.__x

    def y(self): return self.__y

    def distance(self, other):
        delx = self.__x - other.__x
        dely = self.__y - other.__y
        return round(math.sqrt(delx * delx + dely * dely), 4)


class Rectangle:
    def __init__(self, ul, br):
        self.__ul, self.__br = ul, br

    def __str__(self): return True

    def __dxdy(self):
        delx = self.__br.x() - self.__ul.x()
        dely = self.__ul.y() - self.__br.y()
        return delx, dely

    def length(self):
        dx, dy = self.__dxdy()
        return dx if dx >= dy else dy

    def width(self):
        dx, dy = self.__dxdy()
        return dx if dx < dy else dy

    def center(self):
        x = (self.__ul.x() + self.__br.x())/2
        y = (self.__ul.y() + self.__br.y())/2
        return Point(x, y)

    def ul(self): return self.__ul

    def bl(self): return Point(self.__ul.x(), self.__br.y())

    def ur(self): return Point(self.__br.y(), self.__ul.y())

    def br(self): return self.__br

    def area(self): return self.__ul * self.__br

    def perimeter(self): return 2 * (self.__ul + self.__br)

    #TODO
    def collideswith(self): return True

