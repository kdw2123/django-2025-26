class Car:
    def __init__(self,make):
        self.make = make 
    def get_mark(self):
        return self.make
obj = Car("make")
print(obj.get_mark())
        