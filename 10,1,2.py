import math
class Rectaangle:
    def __init__(self,a,b,width,height):
        self.a = a
        self.b = b
        self.width = width
        self.height = height
    def get_Rectangle(self):
        rectSp = [self.a, self.b, self.width, self.height]
        RectRet = "Rectangle ("+", ".join(map(str, rectSp))+")"
        # RectRet = "Rectangle ("+str(self.a)+str(self.b)+str(self.width)+str(self.height)+")"
        return RectRet
class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b
# 10.1
rect_1 = Rectaangle(3,4,30,50)
print(rect_1.get_Rectangle())
#10.2
rect_2 = Rectaangle(3,4)
print(rect_2.get_area())
