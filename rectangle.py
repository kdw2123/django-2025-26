class Rectangle:
    def __init__(self,w,h):
        self.w = w
        self.h = h
    def area(self):
        
        return self.w * self.h
obj = Rectangle(29,12)
print(obj.area())