class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary 
    def annual_salary(self):
        
        return f"name: {self.name} \n salary :  {self.salary *12}"
obj = Employee("kebede",1000)
print(obj.annual_salary())