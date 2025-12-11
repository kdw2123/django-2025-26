class Animal :
    def __init__(self,name,sound):
        self.name = name 
        self.sound = sound
    def make_sound(self):
        return f" name : {self.name} \n sound : {self.sound}"
class Cat(Animal):
    def __init__(self, name, sound,color):
        
        super().__init__(name, sound)
        self.color = color
    def make_sound(self):
        return f"{self.name} {self.color} {self.sound}"
obj1 = Animal("lion", "guaaaaaaaa")
obj2 = Cat("wero","meiaaw","white")
print(obj1.make_sound())
print(obj2.make_sound())