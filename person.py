class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def main(self):
        return f"name : {self.name}  age : {self.age}"
m1 = person("kebi",10)
print(m1.main())