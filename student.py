class Student:
    def __init__(self,age):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,new_age):
      self._age = new_age
obj = Student(10)
print(obj.age)
obj.age = 69
print(obj.age)

    
        