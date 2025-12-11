class Dog:
    def __init__(self,sound):
        self.sound = sound
    def bark(self):
        return f"{self.sound}"
obj = Dog("woof!")
print(obj.bark())
        